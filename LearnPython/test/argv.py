# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from time import ctime
import sys
import random


print 'you entered', len(sys.argv), 'arguments...'
print 'they were: ', str(sys.argv)

print random.choice(range(0, 3))

# print 'ddddd'   \
#       '\nddd'
# dd = "dd"
# DATA = ['你制帐吗？', '你贩剑吗？', '你撞壁吗？']
# print '[%s] %s' % (ctime(), dd), dd, '\n[%s] %s' % (ctime(), dd), DATA[random.choice(range(0, 3))]
#
#
#
# '\n[%s] ' % (ctime(), data), DATA[random.choice(range(0, 3))]