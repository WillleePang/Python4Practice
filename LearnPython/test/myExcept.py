# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'object type cannot be converted to float'
    return retval

def except11():
    try:
        float([])
    except TypeError, diag:
        print str(diag)
        print diag.__class__
        print diag.__class__.__doc__
        print diag.__class__.__name__



if __name__ == '__main__':
    print safe_float('foo')
    print safe_float(123123)
    print safe_float(())
    except11()
