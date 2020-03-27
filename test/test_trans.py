from ..源码 import trans
def testSplitComment():
    src = '''
# comment
pass
   # comment
pass # comment
pass#comment
\'\'\'
comment
\'\'\'
pass
"""
comment
"""
pass
    '''
    src_array = trans.splitComment(src)
    assert src_array == ['\n', '# comment', '\npass\n   ', '# comment', '\npass ', '# comment', '\npass', '#comment', '\n\'\'\'\ncomment\n\'\'\'\npass\n"""\ncomment\n"""\npass\n    ']

def testSplitMultilineString1():
    src = '''qwer
\'\'\'
comment
\'\'\'
asdf'''
    assert trans.splitMultilineString(src) == ['qwer\n',"'''\ncomment\n'''", '\nasdf']

def testSplitMultilineString2():
    src = '''qwer
"""
co''\''mment
"""
asdf'''
    assert trans.splitMultilineString(src) == ['qwer\n','"""\nco\'\'\'\'mment\n"""', '\nasdf']

def testSplitMultilineString3():
    src = '''qwer
"""
comment
"""
asdf
"""
comment
"""
asdf'''
    assert trans.splitMultilineString(src) == ['qwer\n','"""\ncomment\n"""', '\nasdf\n','"""\ncomment\n"""', '\nasdf']

def testSplitString1():
    src='asdf"ab\'c"zxcv'
    assert trans.splitString(src)== ['asdf', '"ab\'c"', 'zxcv']

def testSplitString2():
    src='asdf\'ab"c\'zxcv'
    assert trans.splitString(src)== ['asdf', "'ab\"c'", 'zxcv']
    
def testSplitString3():
    src='asdf"abc"zxcv\'abc\''
    assert trans.splitString(src)== ['asdf', '"abc"', 'zxcv', "'abc'", '']
    
def testChangeKeywords1():
    assert trans.changeKeywords('打印("你好,世界")') == 'print("你好,世界")'

def testChangeKeywords2():
    assert trans.changeKeywords('#打印("你好,世界")') == '#打印("你好,世界")'

def testChangeKeywords3():
    assert trans.changeKeywords('"打印("你好,世界")"') == '"打印("你好,世界")"'

def testChangeKeywords4():
    assert trans.changeKeywords('\'打印("你好,世界")\'') == '\'打印("你好,世界")\''


def testChangeKeywords5():
    assert trans.changeKeywords('打印好("你好,世界")') == '打印好("你好,世界")'





