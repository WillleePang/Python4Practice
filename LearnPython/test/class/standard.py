# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class RoundFloat(float):
    def __new__(cls, val):
        return float.__new__(cls, round(val, 2))


class RoundFloat1(float):
    def __new__(cls, val):
        return super(RoundFloat1, cls).__new__(cls, round(val, 2))


class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68),('xin-yi', 2)))
print 'By iterator:'.ljust(12), [key for key in d]
print 'By keys():'.ljust(12), d.keys()