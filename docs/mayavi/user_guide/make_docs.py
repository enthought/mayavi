"""
Script to generate the docs.

Currently you need to generate the mlab reference using mlab_docs.py
before running this script. This will change in the long run as both
scripts are merged.
"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


# Standard library imports.
import os, shutil, sys, glob

from rst2html_no_include import HTMLCompiler

# The stylesheet used in the generated HTML.
STYLESHEET = 'mayavi.css'
# The stylesheet used in the generated LaTeX
LATEX_STYLESHEET = 'mayavi.tex'
OUT_DIR = 'html'

###############################################################################
# Documentation building functions.
def rst2pdf(filename):
    filename = filename[:-4]
    os.system(
    'rst2newlatex --report=3 %s.rst --user-stylesheet=%s > %s.tex' 
        % (filename, LATEX_STYLESHEET, filename))
    os.system('pdflatex %s.tex' % filename)
    # Run twice for toc
    os.system('pdflatex %s.tex' % filename)
    for ext in ('tex', 'out', 'aux', 'log'):
        os.remove(filename + '.' + ext)

def make_api_docs():
    """ Make the API documentation. """

    try:
        os.makedirs('html/api')

    except:
        pass
    
    # Now make the API documentation.
    print 'Making API documentation...',
    os.system('endo --rst -d html/api -r %s' % os.path.join('..', 'enthought'))
    print 'Done.'

def copy_files_to_dir(dir, from_dir='.', html_only=False):
    """ Copy all files to out directory """
    if from_dir == '.':
        from_dir = ''
    else:
        from_dir += os.sep

    print 'Copying files to %s...' % dir,
    try:
        os.mkdir(dir)
    except:
        pass

    files = glob.glob('%s**/*' % from_dir) + glob.glob('%s*' % from_dir)

    for filename in (a_file for a_file in files if os.path.isdir(a_file)):
        only_filename = filename[len(from_dir):]
        if filename == dir:
            continue
        try:
            os.mkdir('%s/%s' % (dir, only_filename))
        except:
            pass

    for filename in (a_file for a_file in files if not os.path.isdir(a_file)):
        if (filename[-4:] == '.svn' or filename.split(os.sep)[0] == dir
                or filename[-1] == '~'):
            continue
        if html_only and not ( 
                os.path.splitext(filename)[1] in 
                ('.html', '.css', '.jpg', '.gif', '.png')):
            continue
        only_filename = filename[len(from_dir):]
        shutil.copyfile('%s' % filename,'%s/%s' % (dir, only_filename))
    
    print 'Done.'

def copy_images(dir):
    """ Copy any images into the dir directory. """

    # Copy over any images.
    if os.path.isdir('images'):
        print 'Copying images...',
        try:
            os.mkdir('%s/images' % dir)
            
        except:
            pass

        for filename in os.listdir('images'):
            if filename == '.svn':
                continue
        
            shutil.copyfile('images/%s' % filename,'%d/images/%s' % 
                    (dir, filename) )
        print 'Done.'
        
###############################################################################
def main(argv=sys.argv):
    """ Application entry point. """

    # If an additional argument is specified then use it as the stylesheet
    # name.
    if len(argv) > 1:
        stylesheet = argv[1]

    else:
        stylesheet = STYLESHEET

    copy_files_to_dir(OUT_DIR)
    os.chdir(OUT_DIR)

    rst2pdf('user_guide.rst')
    shutil.move('user_guide.pdf', '../user_guide.pdf')
    tmpdir = os.tmpnam()
    try:
        os.mkdir(tmpdir)
    except:
        pass
    HTMLCompiler(dir=tmpdir, stylesheet=stylesheet).compile('user_guide.rst')
    for filename in glob.glob('%s/*.html' % tmpdir):
        shutil.copyfile(filename, './%s' % os.path.basename(filename))
    # Copy files to directory in Mayavi2 Python source for interactive help
    os.chdir('..')
    print os.getcwd()
    HELP_DIR = "../../enthought/mayavi/html"
    copy_files_to_dir(HELP_DIR, from_dir=OUT_DIR, html_only=True)
    #make_api_docs()
    #copy_images('html')
    
    return


if __name__ == '__main__':
    main()

#### EOF ######################################################################
