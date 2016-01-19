# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from time import time, ctime

class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return "self.__data"

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data, attr)


class TimedWrapMe(object):
    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or \
                t_type not in 'cma':
            raise TypeError, \
            "argument of 'c', 'm', or 'a' req'd"
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return "self.__data"

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)

if __name__ == "__main__":
    twm = TimedWrapMe(932)
    print twm.gettimestr('c')
    print twm.gettimestr('m')
    print twm.gettimestr('a')
    print twm
    print twm.gettimestr('c')
    print twm.gettimestr('m')
    print twm.gettimestr('a')
    twm.set('time is up!')
    print twm.gettimestr('m')
    print twm
    print twm.gettimestr('c')
    print twm.gettimestr('m')
    print twm.gettimestr('a')
    print type(WrapMe)
