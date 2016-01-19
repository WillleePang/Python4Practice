# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


import socket


tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tcpSocket.bind()
tcpSocket.listen()
