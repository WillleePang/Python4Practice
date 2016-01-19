# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

db = {}


def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('password: ')
    db[name] = pwd


def olduser():
    name = raw_input('login:　')
    pwd = raw_input('password: ')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'login incorrect'


def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User login
    (Q)uit

    Enter choice:
    '''
    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()


if __name__ == '__main__':
    showmenu()