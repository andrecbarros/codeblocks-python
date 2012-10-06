# client-side test program for interp.py

import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
# Print list of available methods
for m in s.system.listMethods():
    print m
import numpy
numpy.array
s.tag_gen('.')
import os.path
os.path.abspath
fullPath=os.path.abspath('./cbpycomp_client.py')
##origSource=open(fullPath,'r').read()
lineNo=13
origCol=9

s.load_stdlib('STDLIB')
print 'os#######################'
for c in s.complete_phrase('os'):
    print c
print 'os.path.#################'
for c in s.complete_phrase('os.path.'):
    print c
##s.get_completions(fullPath, origSource, lineNo, origCol)