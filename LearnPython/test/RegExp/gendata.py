# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


from random import randint, choice
from string import ascii_lowercase
from sys import maxint
from time import ctime
import re


doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5, 10)):
    dtint = randint(0, maxint - 1)
    dtstr = ctime(dtint)

    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(ascii_lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(ascii_lowercase)

    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)


data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
patt1 = '^\w{3}'
patt2 = '^(\w){3}'
patt3 = '\d+-\d+-\d+'
patt4 = '.+(\d+-\d+-\d+)'
patt5 = '.+?(\d+-\d+-\d+)'
patt6 = '-(\d+)-'
m = re.match(patt1, data)
print m.group()
n = re.search(patt6, data)
print n.group()
print n.group(1)






