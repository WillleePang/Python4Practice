# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class HotelRoomCalc(object):
    'Hotel room rate calculator'

    def __init__(self, rt, sales = 0.085, rm = 0.1):
        '''HotelRoomCalc default arguments
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        daily = round((self.roomRate * (1 + self.salesTax + self.salesTax)), 2)
        return float(days) * daily


class C(object):
    version = 1

c = C()
print c.version
c.version = 3
print c.version
C.version = 10
print c.version
# print C.version, c.version
# c.version += 1
# print C.version, c.version
# C.version += 1
# print C.version, c.version
# print C.__dict__, c.__dict__
