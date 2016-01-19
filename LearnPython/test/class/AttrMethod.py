# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class MyClass(object):
    def __init__(self):
        self.foo = 100


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float)
        "value must be a float"
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)


myInst = MyClass()
print dir(myInst)
print vars(myInst)
print RoundFloatManual(42.0)
# hasattr(myInst, "foo")
# getattr(myInst, "foo")
# hasattr(myInst, "bar")
# getattr(myInst, "bar")
