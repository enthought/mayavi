"""
Module that provides an html compiler for rst documents where the include
directive is not followed, and the target files are compiled in seperate
pages.

usage:

compiler = HTMLCompiler(dir='outdir', stylesheet='stylesheet.css')

compiler.compile('file.rst')

"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


# Standard library imports.
import os, shutil, sys

import re

from docutils.parsers.rst import Parser
from docutils.utils import new_document
from docutils.nodes import section, literal_block

###############################################################################
# Compiling rst with include directives as external links
def parse_no_include(string):
    """ Parses a string and return the document structure, with includes
        disabled.
    """
    P = Parser()
    doc = new_document('')
    # This is probably necessary due to a bug in docutils
    doc.settings.tab_width = 4
    doc.settings.pep_references = False
    doc.settings.rfc_references = False
    doc.settings.file_insertion_enabled = False
    doc.settings.raw_enabled    = True
    P.parse(string, doc)
    return doc

def extract_toc(doc, depth=0):
    """ Generator to iterate on all the section of a docutils document.
        Adds some depth information on the section object.
    """
    for child in doc.children:
        if isinstance(child, section):
            child.depth = depth
            yield child
        for child in extract_toc(child, depth=depth+1):
            yield child

def extract_sections(filename):
    """ Extracts the sections out of a document, returns a list of 
        dictionnaries for each section: depth, title, link id.
    """
    doc = parse_no_include(file(filename).read())
    outlist = []
    for sec in extract_toc(doc):
        if len(sec['names']) > 0:
           outlist.append({ 'name'      : sec['names'][0],
                    'depth'     : sec.depth,
                    'id'       : sec['ids'][0],
                    'filename'  : filename
                  })
    return outlist

def rst2html(filename, stylesheet=None):
    # A template for the command that runs 'rst2html'.
    COMMAND_TEMPLATE = """

    rst2html --report=3  "%s" %s > "%s.html"

    """
    if stylesheet:
        options = "--stylesheet=%s" % stylesheet
    else:
        options = ""
    name, ext = os.path.splitext(filename)
    print >>sys.stderr, 'Processing %s...' % filename,
    os.system(COMMAND_TEMPLATE % (options, filename, name))
    print >>sys.stderr, 'Done.'

def replace_includes(string):
    """ Replace all include directives by links to the target file.
        Returns the modified string, and the list of files to be
        included.
    """
    doc = parse_no_include(string)
    literal_list = [i for i in doc.traverse() 
                        if isinstance(i, literal_block)]
    
    include_files = []

    for item in literal_list:
        matchobj = re.match(r'\.\. include:: (.*)\n', item.astext())
        if matchobj:
            include_file = matchobj.groups()[0]
            include_files.append(include_file)
            sections = extract_sections(include_file)
            sec_strings = []
            for sec in sections:
                sec['name'] = sec['name'][0].upper() + sec['name'][1:] 
                sec_strings.append( """



    <div class='toc%i'><a class='toc%i' href='%s#%s'>
    %s
    </a></div>

"""  % ( 
                                                sec['depth'], 
                                                sec['depth'], 
                                                sec['filename'][:-4]+'.html',
                                                sec['id'],
                                                sec['name'],
                                             ) )
            sec_string = """
            
.. raw:: html
            """ + '\n\n'.join(sec_strings) + "\n\n"
            string = re.sub("\n"+ re.escape(item.rawsource.rstrip()), 
                                sec_string, string)
    return string, include_files


class HTMLCompiler(object):
    """ Class to compile a rst file in an html file, transforming all the
        include directives as links recursively following them.
    """

    def __init__(self, dir='html', stylesheet=None):
        self.dir = dir
        self.stylesheet = stylesheet
        self.files_to_process = set()
        self.back_refs = {}

    def generate_new_rst(self, filename):
        """ Create a new rst file in the destination dir, that will be
            modified to remove the includes and to correct for the broken
            links.
        """
        print >>sys.stderr, "Removing include directives for %s ..." % filename,
        string = file(filename).read()
        string, included_files = replace_includes(string)
        outfilename = self.dir + os.sep + filename
        outfile = file(outfilename, 'w')
        outfile.write(string)
        outfile.close()
        self.files_to_process.update([outfilename, ])
        print >>sys.stderr, "Done."
        for this_filename in included_files:
            self.back_refs[self.dir + os.sep + this_filename] = filename
            self.generate_new_rst(this_filename)

    def extract_targets(self, filename):
        """ Extracts all the targets of a rst document.
        """
        outlist = []
        short_filename = filename[(len(self.dir)+1):-4]
        doc = parse_no_include(file(filename).read())
        for id, item in doc.ids.iteritems():
                if len(item['names'])==0:
                    continue
                if 'refuri' in item:
                    target = item['refuri']
                else:
                    target = "%s.html#%s" % (short_filename, id)
                outlist.append('.. _`%s` : %s' % (
                                    item['names'][0], target) )
        return '\n'.join(outlist)

    def build_link_table(self):
        """ Scans all the rst files intented for html to build a table of the 
            different links to section titles.
        """
        link_table = {}
        for filename in self.files_to_process:
            print >>sys.stderr, "Scanning %s for links..." % filename,
            link_table[filename] = self.extract_targets(filename)
            print >> sys.stderr, "Done."

        return link_table

    def compile(self, filename):
        if self.dir=='.':
            print "!! Warning: compiling will modify inplace the rst files"
        try:
            os.mkdir(self.dir)
        except:
            pass

        stylesheetname = self.dir + os.sep +  self.stylesheet
        if self.stylesheet and not self.dir=='.':
            shutil.copyfile(self.stylesheet, stylesheetname)
        
        self.files_to_process = set()
        self.back_refs = {}

        self.generate_new_rst(filename)
        
        link_table = self.build_link_table()

        for this_filename in self.files_to_process:
            # Create a table of the links not in this file
            this_link_table = []
            for a_filename in link_table:
                if not a_filename == this_filename:
                    this_link_table.append(link_table[a_filename])
            this_link_table =  set(this_link_table)
            this_link_table = '\n\n'.join(this_link_table)


            if this_filename == self.dir + os.sep + filename:
                file(this_filename, 'a').write("\n\n"+this_link_table)
            else :
                # If this is not the top level file, create a link to it.
                links = """

.. raw:: html

    <div class=navigation>
    <a class='navigation' href='%s.html'>
    <img src="images/previous.png" border=0>
    Up </a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a class='navigation' href='%s.html'><img src="images/go-up.png" border=0>
    Top Level</a>
    </div>

        """ % ( self.back_refs[this_filename][:-4], filename[:-4]) 
                footer = """

.. raw:: html

    <br>


%s

%s

""" %  (links, this_link_table)

                header = """
%s
_____

""" % (links)
                string = file(this_filename, 'r').read()

                file(this_filename, 'w').write(header + string + footer)
            
            rst2html(this_filename, stylesheet=stylesheetname)


#### EOF ######################################################################
