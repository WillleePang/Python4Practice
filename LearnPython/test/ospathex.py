# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


import os


for tmpdir in('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break

else:
    print 'no temp directory available'
    tmpdir = ''


if tmpdir:
    # Change the current working directory to path.
    os.chdir(tmpdir)
    # Return a string representing the current working directory.
    cwd = os.getcwd()
    print '*** current temporary directory'
    print cwd


    print '*** creating example directory...'
    # Create a directory named path with numeric mode mode.
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory: '
    print cwd
    print '*** original directory listing: '
    # Return a list containing the names of the entries in the directory given by path.
    print os.listdir(cwd)


    print '*** creating test file...'
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** updated directory listing: '
    print os.listdir(cwd)


    print "*** renaming 'test' to 'filetest.txt'"
    # Rename the file or directory src to dst.
    os.rename('test', 'filetest.txt')
    print '*** updated directory listing: '
    print os.listdir(cwd)


    # Join one or more path components intelligently.
    path = os.path.join(cwd, os.listdir(cwd)[0])
    print '*** full file pathname'
    print path
    print '*** (pathname, basename) =='
    print os.path.split(path)
    print '*** (filename, extension) =='
    print os.path.splitext(os.path.basename(path))


    print '*** displaying file contents: '
    fobj = open(path)
    for eachLine in fobj:
        print eachLine
    fobj.close()


    print '*** deleting test file'
    os.remove(path)
    print '*** updated directory listing: '
    print os.listdir(path)
    os.chdir(os.pardir)
    print '*** deleting test directory'
    os.rmdir('example')
    print '*** DONE'