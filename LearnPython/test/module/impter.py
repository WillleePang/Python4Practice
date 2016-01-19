# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from __future__ import absolute_import

from imptee import foo, show


show()

foo = 123

print 'foo from impter:', foo

show()


def foo():
    print '\ncalling foo()...'
    aString = 'bar'
    anInt = 42
    print "foo()'s globals:", globals().keys()
    print "foo()'s locals:", locals().keys()
print "__main__'s globals:", globals().keys()
print "__main__'s locals:", locals().keys()

