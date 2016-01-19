# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from socket import *
from time import ctime
import random

DATA = ['你制帐吗？', '你贩剑吗？', '你撞壁吗？']
HOST = ''
PORT = 21567
BUFSIZ = 4096
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    message1 = '[%s]阿屎： %s' % (ctime(), data)
    message2 = '\n[%s]机器人： %s' % (ctime(), DATA[random.choice(range(0, 3))])
    message = message1 + message2
    udpSerSock.sendto(message, addr)
    print '...received from and returned to:', addr
udpSerSock.close()