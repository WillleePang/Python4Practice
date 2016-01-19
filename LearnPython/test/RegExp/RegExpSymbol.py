# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

import re


print '='*20
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print m.group()
else:
    print None

m = re.match(bt, 'blt')
if m is not None:
    print m.group()
else:
    print None

m = re.match(bt, 'He bit me!')
if m is not None:
    print m.group()
else:
    print None

m = re.search(bt, 'He bit me!')
if m is not None:
    print m.group()
else:
    print None


print '='*20
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print m.group()
else:
    print None

m = re.match(anyend, 'end')
if m is not None:
    print m.group()
else:
    print None

m = re.match(anyend, '\nend')
if m is not None:
    print m.group()
else:
    print None

m = re.search(anyend, 'The end.')
if m is not None:
    print m.group()
else:
    print None


print '='*20
patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt, '3.14')
if m is not None:
    print m.group()
else:
    print None

m = re.match(patt314, '3014')
if m is not None:
    print m.group()
else:
    print None

m = re.match(patt314, '3.14')
if m is not None:
    print m.group()
else:
    print None


print '='*20
m = re.match("[cr][23][dp][o2]", "c3po")
if m is not None:
    print m.group()
else:
    print None

m = re.match("[cr][23][dp][o2]", "c2do")
if m is not None:
    print m.group()
else:
    print None

m = re.match('r2d2|c3po', 'c2do')
if m is not None:
    print m.group()
else:
    print None

m = re.match('r2d2|c3po', 'r2d2')
if m is not None:
    print m.group()
else:
    print None


print '='*20
patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print m.group()
else:
    print None

m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print m.group()
else:
    print None

m = re.match('\w+@(\w+\.)*\w+\.com', 'nobody@www.yyyy.zzzz.xxx.com')
if m is not None:
    print m.group()
else:
    print None

m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print m.group()
else:
    print None

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print m.group()
else:
    print None


print '='*10, '新世界的大门开始了', '='*10
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print m.group()
print m.group(1)
print m.group(2)
print m.groups()
m = re.match('(a(b))', 'ab')
print m.group()
print m.group(1)
print m.group(2)
print m.groups()


print '='*10, '新世界的大门开始了', '='*10
m = re.search('^The', 'The end.')
if m is not None:
    print m.group()
else:
    print None

m = re.search('^The', 'end. The')
if m is not None:
    print m.group()
else:
    print None

m = re.search(r'\bthe', 'the bite the dog')
if m is not None:
    print m.group()
else:
    print None

m = re.search(r'\bthe', 'bitthe dog')
if m is not None:
    print m.group()
else:
    print None

m = re.search(r'\Bthe', 'bitethe biteddthe dog')
if m is not None:
    print m.group()
else:
    print None




