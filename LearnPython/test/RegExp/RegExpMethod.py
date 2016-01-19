# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

import re


print '='*10, 'findall()', '='*10
m = re.findall(r'\d\d\d', '134-789-654')
if m is not None:
    print m
else:
    print None

print '='*10, 'sub()', '='*10
m = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
n = re.sub('[ae]', 'X', 'abcdef')
if m is not None:
    print m
    print n
else:
    print None

print '='*10, 'subn()', '='*10
m = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
n = re.subn('[ae]', 'X', 'abcdef')
if m is not None:
    print m
    print n
else:
    print None

print '='*10, 'spilt()', '='*10
m = re.split(':', 'str1:str2:str3')
if m is not None:
    print m
else:
    print None


