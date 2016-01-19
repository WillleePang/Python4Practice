# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


@staticmethod
def foo():
    'foo()--properly created doc string'


def bar():
    pass


bar.__doc__ = 'oops, forgot the doc str above'
bar.version = 0.1