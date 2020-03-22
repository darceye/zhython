#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
def splitComment( str):
    return re.split(r'(#.*)', str, re.MULTILINE|re.S)
def splitMultilineString( str):
    return re.split(r'(?:("""|\'\'\')[\s\S]+?\1|("|\')(?:\\.|(?!\2)[^\\\r\n])*\2)', str, re.MULTILINE|re.S)
    

def read( filename):
    return open(sys.argv[1], 'r', encoding='utf-8').read()

        
src = '''
pass
"""
comment
comment
"""
pass
    '''
src_array = splitMultilineString(src)
print(src_array)