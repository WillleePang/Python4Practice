# -*- encoding: utf-8 -*-
# Filename:cardrun

__author__ = 'pangwilllee'

from ___future__ import with_statement


def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval


def main():
    'handles all the data processiong'
    log = open('file\cardlog.txt', 'w')
    try:
        ccfile = open('file\carddata.txt', 'r')
    except IOError, e:
        log.write('no txns in this month\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data...process %s\n' % result)
        else:
            log.write('ignored: %s\n' % result)
    print '$%.2f (new balance)' % total
    log.close()


if __name__ == '__main__':
    main()











