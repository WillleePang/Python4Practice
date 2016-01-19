# -*- encoding: utf-8 -*-
# Filename:stack.py

__author__ = 'pangwilllee'

stack = []


def push_it():
    stack.append(raw_input(' Enter New string: ').strip())


def pop_it():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack'
    else:
        print 'Rmoved [', `stack.pop()`, ']'


def view_stack():
    print stack


CMDs = {'u': push_it, 'o': pop_it, 'v': view_stack}


def show_menu():
    pr = '''
    p(U)sh
    p(O)p
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
            if choice not in 'uovq':
                print 'Invalid option,try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    show_menu()