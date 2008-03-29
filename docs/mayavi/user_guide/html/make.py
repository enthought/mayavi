from docutils.parsers.rst import Parser
from docutils.utils import new_document
from docutils.nodes import section, literal_block

import re

filename = 'auto_mlab_reference.rst'

P = Parser()
doc = new_document('')
# This is probably necessary due to a bug in docutils
doc.settings.tab_width = 4
doc.settings.pep_references = False
doc.settings.rfc_references = False
doc.settings.file_insertion_enabled = False
P.parse(file(filename).read(), doc)

outlist = []

def extract_includes(doc):
    include_files = []
    for item in doc.traverse():
        if not isinstance(item, literal_block):
            continue
        matchobj = re.match(r'\.\. include:: (.*)\n.*', item.astext())
        if matchobj:
            include_file = matchobj.groups()[0]
            include_files.append(include_file)
            print '|%s|' % item.rawsource
        else:
            print item.astest()

    return include_files 

print "found :"

outlist = extract_includes(doc)
print '\n'.join(outlist)

