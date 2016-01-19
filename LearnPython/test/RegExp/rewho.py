# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

import os
import re



f = open('whodata.txt', 'r')
for eachLine in f.readlines():
    print re.split('\s\s+|\t', eachLine.strip())
f.close()