# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


j, k = 1, 2


def proc1():
    j, k = 3, 4
    print 'j == %d and k == %d' % (j, k)


def proc2():
    j = 6
    proc1()
    print 'j == %d and k == %d' % (j, k)


k = 7
proc1()
print 'j == %d and k == %d' % (j, k)

j = 8
proc2()
print 'j == %d and k == %d' % (j, k)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

print factorial(1), factorial(10)


def simpleGen():
    yield 1
    yield '2-->punch!'

my = simpleGen()
print my.next()
print my.next()


from random import randrange


def randGen(aList):
    while aList:
        yield aList.pop(randrange(len(aList)))


for item in randGen(['rock', 'paper', 'scissors']):
    print item


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


count = counter(5)
print count.next()
print count.next()
print count.send(9)
