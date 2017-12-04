# coding=utf-8
import re

''' 
 ?匹配零次或一次前面的分组。
 *匹配零次或多次前面的分组。
 +匹配一次或多次前面的分组。
 {n}匹配n 次前面的分组。
 {n,}匹配n 次或更多前面的分组。
 {,m}匹配零次到m 次前面的分组。
 {n,m}匹配至少n 次、至多m 次前面的分组。
 {n,m}?或*?或+?对前面的分组进行非贪心匹配。
 ^spam 意味着字符串必须以spam 开始。
 spam$意味着字符串必须以spam 结束。
 .匹配所有字符，换行符除外。
 \d、\w 和\s 分别匹配数字、单词和空格。
 \D、\W 和\S 分别匹配出数字、单词和空格外的所有字符。
 [abc]匹配方括号内的任意字符（诸如a、b 或c）。
 [^abc]匹配不在方括号内的任意字符。
'''


def sstrip(text, pattern=''):
    if pattern:
        s = re.compile(pattern)
        return s.sub('', text)
    ss = re.compile('^\s*')
    se = re.compile(r'(\s+)$')
    text = ss.sub('', text)
    text = se.sub('', text)
    ss.findall()
    return text


message = '   Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.   '
print(sstrip(message))
print(sstrip(message, '5'))
