"""
Render the examples to images and adds them to the documentation.
"""

# Standard library imports
import glob
import os
import shutil
import token, tokenize
import textwrap
import itertools

# Enthought imports
from mayavi import mlab

# A global counter, for subsitutions.
global_counter = itertools.count()

EXAMPLE_DIR = '../../examples/mayavi'

def is_mlab_example(filename):
    tokens = tokenize.generate_tokens(open(filename).readline)
    code_only = ''.join([tok_content
                            for tok_type, tok_content, _, _, _  in tokens
                            if not token.tok_name[tok_type] in ('COMMENT',
                                                                'STRING')])
    return ('mlab.show()' in code_only)


def run_mlab_file(filename, image_file):
    ## XXX: Monkey-patch mlab.show, so that we keep control of the
    ## the mainloop
    old_show = mlab.show
    def my_show(func=None):
        pass
    mlab.show = my_show
    mlab.clf()
    e = mlab.get_engine()
    e.close_scene(mlab.gcf())
    exec(
        compile(open(filename).read(), filename, 'exec'),
        {'__name__': '__main__'}
    )
    mlab.savefig(image_file)
    size = mlab.gcf().scene.get_size()
    for scene in e.scenes:
        e.close_scene(scene)
    mlab.show = old_show


def extract_docstring(filename):
    # Extract a module-level docstring, if any
    lines = open(filename).readlines()
    start_row = 0
    if lines[0].startswith('#!'):
        lines.pop(0)
        start_row = 1

    docstring = ''
    first_par = ''
    li = lines.__iter__()
    li_next = li.__next__ if hasattr(li, '__next__') else li.next
    tokens = tokenize.generate_tokens(li_next)
    for tok_type, tok_content, _, (erow, _), _ in tokens:
        tok_type = token.tok_name[tok_type]
        if tok_type in ('NEWLINE', 'COMMENT', 'NL', 'INDENT', 'DEDENT'):
            continue
        elif tok_type == 'STRING':
            docstring = eval(tok_content)
            # If the docstring is formatted with several paragraphs, extract
            # the first one:
            paragraphs = '\n'.join(line.rstrip()
                                for line in docstring.split('\n')).split('\n\n')
            if len(paragraphs) > 0:
                first_par = paragraphs[0]
        break
    return docstring, first_par, erow+1+start_row


################################################################################
# class `ExampleLister`
################################################################################
class ExampleLister(object):
    """ Builds a rst-formatted list of examples from a list of files.
    """
    # Header template, for the example gallery.
    header_tpl = """
%(title)s
--------------------------------------------------

%(intro)s

.. toctree::
   :hidden:

%(toctree)s

.. A comment to split paragraphs

"""

    # Template used to create the example rst file
    example_rst_file_tpl = """

.. _example_%(short_file_name)s:

%(title)s example
--------------------------------------------

%(docstring)s

**Python source code:** :download:`%(short_file_name)s.py`

.. literalinclude:: %(short_file_name)s.py
    :lines: %(end_row)s-


    """

    # The title of the corresponding section in the example gallery.
    title = ''

    # The introductory text of the subsection
    intro =''

    def __init__(self, **kwargs):
        # Cheap unique hash for substitutions
        self._unique_hash = next(global_counter)
        for name, value in kwargs.items():
            setattr(self, name, value)


    def render_all(self, stream, file_list):
        """ Render the example list to the given
            stream (file-like object).
        """
        self._stream = stream
        files_details = self.render_header(file_list)
        for index, file_details in enumerate(files_details):
            filename, short_file_name, short_desc, title, docstring, \
                                                    end_row = file_details
            self.render_example_page(open(os.path.join(self.out_dir,
                                            'example_%s.rst') %
                                     short_file_name, 'w'), index, file_details)
            self.gallery_entry(index, file_details)

        del self._stream


    def render_header(self, filenames):
        files_details = list()
        toctree = list()

        for filename in filenames:
            docstring, short_desc, end_row = extract_docstring(filename)
            short_file_name = os.path.basename(filename)[:-3]
            title = short_file_name.replace('_', ' ')
            title = title[0].upper() + title[1:]
            shutil.copy(filename,
                        os.path.join(self.out_dir, os.path.basename(filename)))


            toctree.append("""   example_%s.rst""" % short_file_name)
            files_details.append((filename, short_file_name, short_desc,
                                        title, docstring, end_row))

        toctree = '\n'.join(toctree)

        title = self.title
        intro = self.intro
        self._stream.write(self.header_tpl % locals())
        return files_details


    def render_example_page(self, stream, index, file_details):
        """ Render an individual example page.
        """
        filename, short_file_name, short_desc, title, docstring, end_row \
                                                                = file_details
        stream.write(self.example_rst_file_tpl % locals())


    def gallery_entry(self, index, file_details):
        """ Write the entry in the main example gallery file
            corresponding to the given file details.
        """
        filename, short_file_name, short_desc, title, docstring, \
                                end_row = file_details
        self._stream.write(
                "\n* :ref:`example_%(short_file_name)s`\n" % locals()
            )
        short_desc = short_desc.lstrip().rstrip()
        for line in short_desc.split('\n'):
            self._stream.write(4*" " + line.lstrip() + "\n")


################################################################################
# class `ImagesExampleLister`
################################################################################
class ImagesExampleLister(ExampleLister):
    """ ExampleLister that looks for thumbnails.
    """

    # Relative directory to images
    images_dir = 'mayavi/images/'

    def render_all(self, stream, file_list):
        self._stream = stream
        files_details = self.render_header(file_list)
        unique_hash = self._unique_hash
        for index, (filename, short_file_name, _, _, _, _) in \
                                        enumerate(files_details):
            image_file = os.path.join(self.images_dir,
                        'example_%(short_file_name)s.jpg' % locals())
            if os.path.exists(image_file):
                short_image_file = os.path.join(*(
                                    image_file.split(os.sep)[1:]))
                self._stream.write("""
.. |%(unique_hash)02i%(index)02i| image:: ../%(short_image_file)s
    :width: 150

            """ % locals())
            else:
                self._stream.write("""
.. |%(unique_hash)02i%(index)02i| raw:: html

    <br/>

            """ % locals())

        self._stream.write(2*('\n' + 7*"=" + " " + 45*"="))

        for index, file_details in enumerate(files_details):
            filename, short_file_name, short_desc, title, docstring, end_row = \
                                                                file_details
            self.render_example_page(open(os.path.join(self.out_dir,
                                        'example_%s.rst') %
                                     short_file_name, 'w'), index, file_details)
            self.gallery_entry(index, file_details)

        self._stream.write("\n"+7*"=" + " " + 45*"=" + '\n')

        del self._stream


    def render_example_page(self, stream, index, file_details):
        """ Hijack this method to, optionally, render images.
        """
        # Jump one step up, and do not call ImagesExampleLister
        filename, short_file_name, short_desc, title, docstring, end_row = \
                                                                file_details
        image_file = os.path.join(self.images_dir,
                        'example_%(short_file_name)s.jpg' % locals())
        if os.path.exists(image_file):
            docstring += """

.. image:: ../%s
    :align: center

""" % os.path.join(*(image_file.split(os.sep)[1:]))

        file_details = \
            filename, short_file_name, short_desc, title, docstring, end_row

        stream.write(self.example_rst_file_tpl % locals())



    def gallery_entry(self, index, file_details):
        filename, short_file_name, short_desc, title, docstring, end_row = \
                                                                file_details
        short_desc = textwrap.wrap(short_desc, width=40)
        unique_hash = self._unique_hash
        self._stream.write(
                ("\n|%(unique_hash)02i%(index)02i|" % locals()).ljust(9) +
                ":ref:`example_%(short_file_name)s`\n" % locals()
            )
        for line in short_desc:
            self._stream.write(9*" " + line.lstrip() + "\n")

################################################################################
# class `MlabExampleLister`
################################################################################
class MlabExampleLister(ImagesExampleLister):

    header_tpl = """
Mlab functions gallery
----------------------

These are the examples of the mlab plotting functions. They are
copied out here for convenience. Please refer to the corresponding
section of the user guide for more information (
:ref:`mlab_plotting_functions`).

.. currentmodule:: mayavi.mlab

+------------------+-------------------------+----------------------+
| :func:`plot3d`   | :func:`points3d`        | :func:`imshow`       |
|                  |                         |                      |
| |plot3d.jpg|     | |points3d.jpg|          | |imshow.jpg|         |
+------------------+-------------------------+----------------------+
| :func:`surf`     | :func:`contour_surf`    | :func:`mesh`         |
|                  |                         |                      |
| |surf.jpg|       | |contour_surf.jpg|      | |mesh.jpg|           |
+------------------+-------------------------+----------------------+
| :func:`barchart` | :func:`triangular_mesh` | :func:`contour3d`    |
|                  |                         |                      |
| |barchart.jpg|   | |triangular_mesh.jpg|   | |contour3d.jpg|      |
+------------------+-------------------------+----------------------+
| :func:`quiver3d` | :func:`flow`            | :func:`volume_slice` |
|                  |                         |                      |
| |quiver3d.jpg|   |  |flow.jpg|             | |volume_slice.jpg|   |
+------------------+-------------------------+----------------------+

.. |plot3d.jpg| image:: ../generated_images/enthought_mayavi_mlab_plot3d.jpg
     :width: 150

.. |points3d.jpg| image:: ../generated_images/enthought_mayavi_mlab_points3d.jpg
     :width: 150

.. |imshow.jpg| image:: ../generated_images/enthought_mayavi_mlab_imshow.jpg
     :width: 150

.. |contour_surf.jpg| image:: ../generated_images/enthought_mayavi_mlab_contour_surf.jpg
     :width: 150

.. |triangular_mesh.jpg| image:: ../generated_images/enthought_mayavi_mlab_triangular_mesh.jpg
     :width: 150

.. |surf.jpg| image:: ../generated_images/enthought_mayavi_mlab_surf.jpg
     :width: 150

.. |mesh.jpg| image:: ../generated_images/enthought_mayavi_mlab_mesh.jpg
     :width: 150

.. |barchart.jpg| image:: ../generated_images/enthought_mayavi_mlab_barchart.jpg
     :width: 150

.. |contour3d.jpg| image:: ../generated_images/enthought_mayavi_mlab_contour3d.jpg
     :width: 150

.. |quiver3d.jpg| image:: ../generated_images/enthought_mayavi_mlab_quiver3d.jpg
     :width: 150

.. |flow.jpg| image:: ../generated_images/enthought_mayavi_mlab_flow.jpg
     :width: 150

.. |volume_slice.jpg| image:: ../generated_images/enthought_mayavi_mlab_volume_slice.jpg
     :width: 150


Advanced mlab examples
-----------------------

.. toctree::
   :hidden:

%(toctree)s

"""

    example_rst_file_tpl = """

.. _example_%(short_file_name)s:

%(title)s example
--------------------------------------------------------------------

%(docstring)s

**Python source code:** :download:`%(short_file_name)s.py`

.. literalinclude:: %(short_file_name)s.py
    :lines: %(end_row)s-


    """

    render_images = False

    images_dir = 'mayavi/generated_images'

    def render_example_page(self, stream, index, file_details):
        """ Hijack this method to, optionally, render images.
        """
        filename, short_file_name, short_desc, title, docstring, end_row = \
                                                            file_details
        if self.render_images:
            print("Generating images for %s" % filename)
            image_file = os.path.join(self.images_dir, 'example_%s.jpg' \
                                    % short_file_name)
            run_mlab_file(filename, image_file=image_file)
        ImagesExampleLister.render_example_page(self, stream,
                                                index, file_details)



################################################################################
# Main entry point
def render_examples(render_images=False, out_dir='mayavi/auto'):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    example_gallery_file = open(os.path.join(out_dir, 'examples.rst'), 'w')

    example_gallery_file.write("""

.. _example_gallery:

Example gallery
=================

""")

    ##########################################################################
    # Mlab examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'mlab', '*.py'))
                    if is_mlab_example(filename)]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))

    mlab_example_lister = MlabExampleLister(render_images=render_images,
                                        out_dir=out_dir,
                                        images_dir='mayavi/generated_images')
    if render_images:
        pass
        # XXX: Add logics to deal with rerendering examples cleverly

    mlab_example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # Interactive application examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'interactive', '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
    example_lister = ImagesExampleLister(
            title="Interactive examples",
            out_dir=out_dir,
            intro="""

Examples showing how to use the interactive features of Mayavi, either
via the mayavi2 application, or via specially-crafted dialogs and
applications.
    """)
    example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # Advanced visualization examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'advanced_visualization', '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
    example_lister = ExampleLister(
            title="Advanced visualization examples",
            out_dir=out_dir,
            intro="""
Data visualization using the core Mayavi API, object-oriented, and with
more fine control than mlab.

    """)
    example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # Data interaction examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'data_interaction', '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
    example_lister = ExampleLister(
            title="Data interaction examples",
            out_dir=out_dir,
            intro="""
Examples showing how you can query and interact with the data.

    """)
    example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # The remaining files
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
    example_lister = ExampleLister(title="Misc examples",
                                   out_dir=out_dir)
    example_lister.render_all(example_gallery_file, example_files)



if __name__ == '__main__':
    render_examples()
    import shutil
    shutil.copyfile('../CHANGES.txt', './mayavi/auto/changes.rst')
