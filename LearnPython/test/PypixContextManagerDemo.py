# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class PypixContextManagerDemo:

    def __enter__(self):
        print 'Entering the block!'

    def __exit__(self, *unused):
        print 'Exiting the block!'

with PypixContextManagerDemo():
    print 'In the block'


class PypixOpen:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.openedFile = open(self.filename, self.mode)
        return self.openedFile

    def __exit__(self, *unused):
        self.openedFile.close()

with PypixOpen("file\unicode.txt", "w") as writer:
    writer.write('Hello, pangwilllee!')