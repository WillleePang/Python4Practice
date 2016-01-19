# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from urllib import urlretrieve


def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine


def firstLast(webPage):
    f = open(webPage)
    lines = f.readlines()
    f.close()
    print firstNonBlank(lines)
    lines.reverse()
    print firstNonBlank(lines)


def download(url='http://www.qq.com', process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)


def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" % (eachKW, kw[eachKW])

if __name__ == '__main__':
    # download()
    newfoo('wolf', 3, 'wwwww', 'worinimei', freud=90, gamble=96,)



