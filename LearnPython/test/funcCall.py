# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


# def foo():
#     print 'in foo()'
#     bar()
#
#
# def bar():
#     print 'in bar()'


def foo():
    def bar():
        print 'bar() called'

    print 'foo() called'
    bar()


if __name__ == '__main__':
    foo()