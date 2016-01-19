# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d :: %r]' % (self.__num, self.__string)
    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num, self.__string + other.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.__num * other, self.__string * other)

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num, other.__num)) + \
               self.__norm_cval(cmp(self.__string, other.__string))


if __name__ == "__main__":
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
    print a, b, c, d, e, f
    print a < b
    print b < c
    print a == a
    print b*2
    print a*3
    print b + e
    print e + b
    if d:
        print 'not false'
    if e:
        print 'not false'
    print cmp(a, b)
    print cmp(a, c)
    print cmp(a, a)