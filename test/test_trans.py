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

def testSplitMultilineString():
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

