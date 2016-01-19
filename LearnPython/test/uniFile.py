# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

CODEC = 'utf-8'
FILE = 'file\unicode.txt'

hello_out = u'Hello world\n'
bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

f = open(FILE)
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)

print hello_in
