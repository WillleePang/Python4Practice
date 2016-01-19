# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from weakref import WeakKeyDictionary


# class NonNegative(object):
#     '''A descriptor that forbids negative values'''
#
#     def __init__(self, default):
#         self.default = default
#         self.data = WeakKeyDictionary()
#
#     def __get__(self, instance, owner):
#         # we get here when someone calls x.d and d is a NonNegative instance
#         # instance = x
#         # owner = type(x)
#         return self.data.get(instance, self.default)
#
#     def __set__(self, instance, value):
#         # we get here when someone calls x.d = val, and d is a NonNegative instance
#         # instance = x
#         # value = val
#         if value < 0:
#             raise ValueError("Negative value not allowed: %s" % value)
#         self.data[instance] = value


# class Movie(object):
#     # always put descriptors at the class-level
#     rating = NonNegative(0)
#     runtime = NonNegative(0)
#     budget = NonNegative(0)
#     gross = NonNegative(0)
#
#     def __init__(self, title, rating, runtime, budget, gross):
#         self.title = title
#         self.rating = rating
#         self.runtime = runtime
#         self.budget = budget
#         self.gross = gross
#
#     def profit(self):
#         return self.gross - self.budget

# m = Movie('Casablanca', 97, 102, 964000, 1300000)
# print m.budget  # calls Movie.budget.__get__(m, Movie)
# m.rating = 100  # calls Movie.budget.__set__(m, 100)
# print m.rating
# try:
#     m.rating = -1   # calls Movie.budget.__set__(m, -100)
# except ValueError:
#     print "Woops, negative value"


# class Broken(object):
#     y = NonNegative(5)
#
#     def __init__(self):
#         self.x = NonNegative(0)  # NOT a good descriptor

# b = Broken()
# print "X is %s, Y is %s" % (b.x, b.y)


# class BrokenNonNegative(object):
#     def __init__(self, default):
#         self.value = default
#
#     def __get__(self, instance, owner):
#         return self.value
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Negative value not allowed: %s" % value)
#         self.value = value
#
#
# class Foo(object):
#     bar = BrokenNonNegative(5)

# f = Foo()
# try:
#     f.bar = -1
# except ValueError:
#     print "Caught the invalid assignment"

# f = Foo()
# g = Foo()
#
# print "f.bar is %s\ng.bar is %s" % (f.bar, g.bar)
# print "Setting f.bar to 10"
# f.bar = 10
# print "f.bar is %s\ng.bar is %s" % (f.bar, g.bar)


# class MoProblems(list):  #you can't use lists as dictionary keys
#     x = NonNegative(5)

# m = MoProblems()
# print m.x  # womp womp


# class Descriptor(object):
#
#     def __init__(self, label):
#         self.label = label
#
#     def __get__(self, instance, owner):
#         print '__get__', instance, owner
#         return instance.__dict__.get(self.label)
#
#     def __set__(self, instance, value):
#         print '__set__'
#         instance.__dict__[self.label] = value


# class Foo(list):
#     x = Descriptor('x')
#     y = Descriptor('y')

# f = Foo()
# f.x = 5
# print f.x


# class Foo1(object):
#     x = Descriptor('y')
#
# f1 = Foo1()
# f1.x = 5
# print f1.x
# f1.y = 4    #oh no!
# print f1.x

# class Descriptor(object):
#     def __init__(self):
#         #notice we aren't setting the label here
#         self.label = None
#
#     def __get__(self, instance, owner):
#         print '__get__. Label = %s' % self.label
#         return instance.__dict__.get(self.label, None)
#
#     def __set__(self, instance, value):
#         print '__set__'
#         instance.__dict__[self.label] = value
#
#
# class DescriptorOwner(type):
#     def __new__(cls, name, bases, attrs):
#         # find all descriptors, auto-set their labels
#         for n, v in attrs.items():
#             if isinstance(v, Descriptor):
#                 v.label = n
#         return super(DescriptorOwner, cls).__new__(cls, name, bases, attrs)
#
#
# class Foo(object):
#     __metaclass__ = DescriptorOwner
#     x = Descriptor()

# f = Foo()
# f.x = 10
# print f.x


class CallbackProperty(object):
    """A property that will alert observers when upon updates"""
    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        for callback in self.callbacks.get(instance, []):
            # alert callback function of new value
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """Add a new function to call everytime the descriptor within instance updates"""
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)


class BankAccount(object):
    balance = CallbackProperty(0)


def low_balance_warning(value):
    if value < 100:
        print "You are now poor"

ba = BankAccount()
BankAccount.balance.add_callback(ba, low_balance_warning)

ba.balance = 5000
print "Balance is %s" % ba.balance
ba.balance = 99
print "Balance is %s" % ba.balance


