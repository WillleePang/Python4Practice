# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


# from time import ctime
#
#
# print '*** Welcome to Metaclasses!'
# print '\tMetaclass declaration first.'
#
#
# class MetaC(type):
#
#     def __init__(cls, name, bases, attrd):
#         super(MetaC, cls).__init__(name, bases, attrd)
#         print '***Created class %r at: %s' % (name, ctime())
#
#
# print '\tClass "Foo" declaration next.'
#
#
# class Foo(object):
#     __metaclass__ = MetaC
#
#     def __init__(self):
#         print '*** Instantiated class %r at: %s' % (self.__class__.__name__, ctime())
#
#
# print '\tClass "Foo" instantiation next.'
# f = Foo()
# print '\tDONE'

from warnings import warn


class ReqStrSugRepr(type):
    def __init__(cls, name, bases, attrd):
        super(ReqStrSugRepr, cls).__init__(name, bases, attrd)

        if '__str__' not in attrd:
            raise TypeError('Class requires overriding of __str__')
        if '__repr__' not in attrd:
            warn('Class suggests overriding of __repr__()\n', stacklevel=3)


print '*** Defined ReqStrSugRepr (meta)class\n'


class Foo(object):
    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        return 'Instance of class:', \
            self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__

print '*** Defined Foo class\n'


class Bar(object):
    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        return 'Instance of class:', \
            self.__class__.__name__

print '*** Defined Bar class\n'


class FooBar(object):
    __metaclass__ = ReqStrSugRepr

print '*** Defined FooBar class\n'