# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


import os, socket, errno, types, tempfile


class NetworkError(IOError):
    pass


class FileError(IOError):
    pass


def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list[args]

    if newarg:
        myargs.append(newarg)

    return myargs


def fileArgs(file, mode, args):
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms =''
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)

    else:
        myargs = args

    return tuple(myargs)


def myconnect(socket, host, port):
    try:
        socket.connect(host, port)
    except socket.error, args:
        myargs = updArgs(args)
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])
        raise NetworkError, updArgs(myargs, host+':'+str(port))


def myopen(file, mode='r'):
    try:
        fo = open(file, mode)
    except IOError, args:
        raise FileError, fileArgs(file, mode, args)

    return fo


def testfile():
    file = tempfile.mktemp()
    f= open(file, 'w')
    f.close()

    for eachTest in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(file, eachTest[0])
            f = myopen(file, eachTest[1])
        except FileError, args:
            print '%s: %s' % (args.__class__.__name__, args)
        else:
            print file, "opened ok... perms ignored"
            f.close()

    os.chmod(file, 0777)
    os.unlink(file)


def testnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for eachHost in('deli', 'www'):
        try:
            myconnect(s, 'deli', 8080)
        except NetworkError, args:
            print '%s: %s' % (args.__class__.__name__, args)


if __name__ == "__main__":
    testfile()
    testnet()




