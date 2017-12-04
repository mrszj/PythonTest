#coding=utf8
import pprint
from itertools import count
spam = {
    'color':'red',
    'age':'42'
    }
# for v in spam.values():
#     print(v)
# for k in spam.keys():
#     print(k)
# for i in spam.items():
#     print(list(i))

# picnicItems = {'aaples':5,'cpus':2}
# print(picnicItems.get('cpusa',0))

spam.setdefault('aa','aaa')


pprint.pprint(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
counta={}
for character in message:
    counta.setdefault(character,0)
    counta[character]=counta[character]+1
pprint.pprint(counta)