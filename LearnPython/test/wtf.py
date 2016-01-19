# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


def hehe():
    count = 1
    while count > 0:
        if count == 10:
            continue
        elif count > 20:
            break
        count += 1
        print 'content num is ', count


def iteList():
    myList = [1, 2, 3, 4, 5]
    for num in myList:
        print num
        myList.remove(num)


def iterDict():
    myDict = {'a': 1, 'b': 2, 'c': 3}
    for key in myDict:
        print key, myDict[key]
        del myDict[key]


def readFile():
    fileUrl = 'file\unicode.txt'
    f = open(fileUrl)
    data = [line for line in f]
    print data


x = 10
def foo():
    y = 5
    bar = lambda z: x+y
    print bar(y)
    y = 8
    print bar(y)

if __name__ == '__main__':
    ##iteList()
    ##iterDict()
    # readFile()
    foo()

