"""This module defines an indenter class that handles indentation
levels for automatic code generation.  It also defines other
miscellaneous classes useful for the tvtk code generation.

"""

# Author: Prabhu Ramachandran
# Copyright (c) 2004-2015, Enthought, Inc.
# License: BSD Style.

import re

# Local imports (there is a good reason for the relative imports).
from .common import get_tvtk_name, camel2enthought


######################################################################
# `Indent` class.
######################################################################

class Indent:
    """This class manages indentation levels for dynamically generated
    Python code.  The class also provides a method that formats a text
    string suitably at a given indentation level.

    """
    def __init__(self, nspace=4):
        """Initializes the object.

        Parameters
        ----------

        - nspace : `int`

          Specifies the number of spaces to use for each indentation
          level. Defaults to 4.

        """
        self.tab = ''
        self.txt = ''
        self.nspace = 0
        self.set_tab(nspace)
        self.space_re = re.compile(r'^\s*$')
        self.find_space_re = re.compile(r'\s*(\S)')

    def __repr__(self):
        return self.txt

    def set_tab(self, nspace):
        """Set the number of spaces a tab represents."""
        self.nspace = nspace
        self.tab = ' '*nspace

    def reset(self):
        """Reset the indentation level to 0."""
        self.txt = ''

    def incr(self):
        """Increase the indentation level."""
        self.txt += self.tab

    def decr(self):
        """Decrease the indentation level."""
        self.txt = self.txt[:-self.nspace]

    def format(self, txt):
        """Formats given text as per current indentation levels.

        Note that the returned string always ends with a newline to
        avoid problems for subsequent lines in the output that have to
        deal trailing garbage in the last line.

        Parameters
        ----------

        - txt : `string`

          Input text string to be formatted.  Can contain newlines.

          If the input text is a single line of text then leading
          space is stripped and the current indentation is added to
          the left along with a newline and the resulting string is
          returned.

          If the input text is multi-line input the indentation of the
          first line is ignored, and the second line is considered.
          All subsequent lines have the current indentation followed
          by any extra space from the default indentation.

        """
        space_re = self.space_re
        find_space_re = self.find_space_re

        d = txt.split('\n')
        one_liner = 1
        if len(d) > 1:
            for i in d[1:]:
                if not space_re.match(i):
                    one_liner = 0
                    break
        elif len(d) == 0:
            return '\n'

        if one_liner:
            return '%s%s\n'%(repr(self), d[0].strip())
        else:
            strip_idx = 0
            m = find_space_re.match(d[1])

            try:
                strip_idx = m.start(1)
            except AttributeError:
                strip_idx = 0
            ret = []
            if not space_re.match(d[0]):
                ret.append('%s%s'%(repr(self), d[0]))
            for i in d[1:]:
                if i:
                    ret.append('%s%s'%(repr(self), i[strip_idx:]))
                else:
                    ret.append(repr(self))

            if space_re.match(ret[-1]):
                ret[-1] = ''
            else:
                ret.append('')
            return '\n'.join(ret)


######################################################################
# `VTKDocMassager` class.
######################################################################

class VTKDocMassager:
    """This class massages the documentation strings suitably for
    inclusion in the TVTK code.  The names of all the VTK classes are
    changed suitably and when possible the method names are also
    changed.

    This class is *not* generic and is *very* specific to VTK
    documentation strings.
    """
    def __init__(self):
        self.renamer = re.compile(r'(vtk[A-Z0-9]\S+)')
        self.ren_func = lambda m: get_tvtk_name(m.group(1))
        self.func_re = re.compile(r'([a-z0-9]+[A-Z])')
        self.cpp_method_re = re.compile(r'C\+\+: .*?;\n*')

    #################################################################
    # `VTKDocMassager` interface.
    #################################################################

    def write_class_doc(self, doc, out, indent):
        """Write processed class documentation string into `out`.

        Parameters
        ----------
        - doc : `string`

          The documentation string.

        - out : file line object.

        - indent : `Indent`
        """
        ret = self.massage(doc)
        indent.incr()
        out.write(indent.format('"""'))
        out.write(indent.format('\n' + ret))
        out.write(indent.format('"""'))
        indent.decr()

    def write_trait_doc(self, doc, out, indent):
        """Write processed trait documentation string into `out`.

        This method removes the call signature information from the
        method.

        Parameters
        ----------
        - doc : `string`

          The documentation string.

        - out : file line object.

        - indent : `Indent`
        """
        ret = self._remove_sig(doc)
        indent.incr()
        out.write(indent.format('"""'))
        out.write(indent.format('\n'+self.massage(ret)))
        out.write(indent.format('"""'))
        indent.decr()

    def write_method_doc(self, doc, out, indent):
        """Write processed method documentation string into `out`.

        The method signature is appopriately massaged.

        Parameters
        ----------
        - doc : `string`

          The documentation string.

        - out : file line object.

        - indent : `Indent`
        """
        orig_name = doc[2:doc.find('(')]
        name = camel2enthought(orig_name)
        my_sig = self._rename_class(doc[:doc.find('\n\n')])
        my_sig = self.cpp_method_re.sub('', my_sig)
        my_sig = my_sig.replace('V.'+orig_name, 'V.'+name)
        indent.incr()
        out.write(indent.format('"""'))
        out.write(indent.format(my_sig))
        ret = self._remove_sig(doc)
        if ret:
            out.write('\n')
            out.write(indent.format('\n'+self.massage(ret)))
        out.write(indent.format('"""'))
        indent.decr()

    def get_method_doc(self, doc):
        """Return processed method documentation string from `doc`.

        The method signature is appopriately massaged.

        Parameters
        ----------
        - doc : `string`

          The documentation string.
        """
        orig_name = doc[2:doc.find('(')]
        name = camel2enthought(orig_name)
        my_sig = self._rename_class(doc[:doc.find('\n\n')])
        my_sig = self.cpp_method_re.sub('', my_sig)
        my_sig = my_sig.replace('V.'+orig_name, 'V.'+name)
        ret = self.massage(self._remove_sig(doc))
        if ret:
            return my_sig + '\n' + ret
        else:
            return my_sig

    def massage(self, doc):
        """Returns massaged documentation string from passed
        docstring, `doc`.  This method basically renames the methods
        and classes in the docstring.
        """
        ret = self._rename_methods(doc)
        ret = self._rename_class(ret)
        return ret

    #################################################################
    # Non-public interface.
    #################################################################

    def _rename_class(self, doc):
        return self.renamer.sub(self.ren_func, doc)

    def _remove_sig(self, doc):
        idx = doc.find('\n\n') + 2
        if len(doc) > idx:
            return doc[idx:]
        else:
            return ''

    def _rename_methods(self, doc):
        lines = doc.split('\n')
        nl = []
        for line in lines:
            words = line.split(' ')
            nw = []
            for word in words:
                if word[:3] == 'vtk':
                    nw.append(word)
                else:
                    if self.func_re.search(word):
                        nw.append(camel2enthought(word))
                    else:
                        nw.append(word)
            nl.append(' '.join(nw))
        return '\n'.join(nl)
