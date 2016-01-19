# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


def fun1(*keys):
    print 'keys type=%s' % type(keys)
    print 'keys=%s' % str(keys)
    for i in range(0, len(keys)):
        print 'key[' + str(i) + ']=%s' % str(keys[i])


def fun2(**keys):
    print 'keys type=%s' % type(keys)
    print 'keys=%s' % str(keys)
    print 'name=%s' % str(keys['name'])



if __name__ == '__main__':
    fun1(2, 3, 4, 5)
    print '='*10, '''(╯°口°)╯(┴—┴''', '='*10
    fun2(name='vp', age=19)