#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
import time
import threading


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s' % addr
    sock.sent('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


