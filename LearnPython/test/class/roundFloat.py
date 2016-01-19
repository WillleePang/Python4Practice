# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class RoundFloatManual(float):
    def __init__(self, val):
        assert isinstance(val, float)
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__

