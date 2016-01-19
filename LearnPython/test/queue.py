# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

queue = []


def en_q():
    queue.append(raw_input(' Enter New string: ').strip())


def del_q():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue!'
    else:
        print 'removed [', `queue.pop(0)`, ']'


def view_q():
    print queue


CMDs = {'e': en_q, 'd': del_q, 'v': view_q}


def show_menu():
    pr = ''''
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit

    Enter choice:'''

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'edvq':
                print 'Invalid option,try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    show_menu()