# -*- encoding: utf-8 -*-
# Filename: using_file.py

__author__ = 'pangwilllee'

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = file(r'D:\files\poem.txt', 'a')  # open for 'w'riting
f.write(poem)
f.close()

f = file(r'D:\files\poem.txt')
# if no mode is specified, 'r'ead mode is assumed by defult
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,
f.close()
