#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re

gKeywordMap = [
    [ '打印', 'print'],
]

def splitComment( str):
    return re.split(r'(#.*)', str, re.MULTILINE|re.S)

def splitMultilineString( str):
    r = r'(?:("""|\'\'\')[\s\S]+?\1|("|\')(?:\\.|(?!\2)[^\\\r\n])*\2)'
    return re.split(r'("""[\s\S]+?"""|\'\'\'[\s\S]+?\'\'\')', str, re.MULTILINE|re.S)

def splitString(str):
    return re.split(r'(\'[\s\S]+?\'|"[\s\S]+?")', str, re.MULTILINE|re.S)

def changeKeywords(str):
    if re.match(r'[\'"#]', str) != None:
        return str
    for keywordPair in gKeywordMap:
        str = re.sub(re.compile('(\W)' + keywordPair[0] + '(\W)', re.L|re.M), '\1' + keywordPair[1] + '\2')
    return str

def read( filename):
    return open(sys.argv[1], 'r', encoding='utf-8').read()

print(changeKeywords('#打印("你好,世界")'))