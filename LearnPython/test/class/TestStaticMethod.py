# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class TestStaticMethod(object):
    @staticmethod
    def foo():
        print 'calling static method foo()'


class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__

