# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print 'Parent'

    def bar(self, message):
        print message, 'from Parent'


class FooChild(FooParent):
    def __init__(self):
        # FooParent.__init__(self)
        super(FooChild, self).__init__()
        print 'Child'

    def bar(self, message):
        # FooParent.bar(self, message)
        super(FooChild, self).bar(message)
        print 'Child bar function.'
        print self.parent


class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"


class B(object):
    def __init__(self):
        print "enter B"
        print "leave B"


class C(A):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"


class D(A):
    def __init__(self):
        print "enter D"
        super(D, self).__init__()
        print "leave D"


class E(B, C):
    def __init__(self):
        print "enter E"
        B.__init__(self)
        C.__init__(self)
        print "leave E"


class F(E, D):
    def __init__(self):
        print "enter F"
        E.__init__(self)
        D.__init__(self)
        print "leave F"


if __name__ == '__main__':
    # fooChild = FooChild()
    # fooChild.bar('HelloWorld')
    f = F()
