# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class MyData(object):
    pass


class MyDataWithMethod(object):
    def printFoo(self):
        print 'You invoked printFoo()!'

    def __del__(self):
        print 'del'


class AddrBookEntry(object):
    'address book entry class'
    foo = 100
    def __init__(self, nm, ph):
        self.name =nm
        self.phone = ph
        print 'Created instance for:', self.name

    def updatePhone(self, newph):
        self.phone = newph
        print 'Updated phone# for:', self.name


class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.id = id
        self.em = em

    def updateEmail(self, newem):
        self.em = newem
        print 'Updated e-mail address for:', self.name





if __name__ == '__main__':
    # mathObj = MyData()
    # mathObj.x = 2
    # mathObj.y = 3
    # print mathObj.x + mathObj.y
    # print mathObj.x * mathObj.y
    #
    # myObj = MyDataWithMethod()
    # myObj.printFoo()

    # print EmplAddrBookEntry.__bases__

    c1 = MyDataWithMethod()
    c2 = c1
    c3 = c2
    del c1
    del c2
    del c3




