# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self._budget = None

        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    # nice
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    # ok
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._rating = value

    # uhh...
    @property
    def runtime(self):
        return self._runtime

    @runtime.setter
    def runtime(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._runtime = value

    # is this forever?
    @property
    def gross(self):
        return self._gross

    @gross.setter
    def gross(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._gross = value

    def profit(self):
        return self.gross - self.budget


m = Movie('Casablance', 97, 102, 964000, 1300000)
print m.budget  # calls m.budget(), returns result
try:
    m.budget = -100  # calls budget.setter(-100), and raises ValueError
except ValueError:
    print "Woops. Not allowed"
