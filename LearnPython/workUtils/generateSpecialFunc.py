# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

import random
import string
import generateName


def generate1(max):
    for i in range(max):
        print 'arr.insert(%d);' % random.randint(0, 100)


def generate2(max):
    for i in range(max):
        # last = ''.join([random.choice(string.lowercase) for i in range(random.randint(3, 10))])
        # first = ''.join([random.choice(string.lowercase) for i in range(random.randint(3, 10))])
        last = generateName.gen_one_gender_word()
        first = generateName.gen_one_gender_word()
        age = random.randint(0, 50)
        print 'arr.insert("%s", "%s", %d);' % (last, first, age)


if __name__ == '__main__':
    generate2(10)