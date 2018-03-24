#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: service.py
socket service
"""


import socket
import threading
import time
import sys

EXIT = b'9'
T_UP = b'1'
T_DOWN = b'2'
T_LEFT = b'3'
T_RIGHT = b'4'
NONE = b'0'

class Server:
    def __init__(self):

    #def socket_service(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind(('127.0.0.1', 6666))
            self.s.listen(10)
            self.trigger = NONE
        except socket.error as msg:
            print (msg)
            sys.exit(1)
        print ( 'Waiting connection...' )

        self.conn, self.addr = self.s.accept()
        self.t = threading.Thread(target=self.deal_data, args=(self.conn, self.addr))
        self.t.start()

    def get_trigger(self):
        return self.trigger

    def set_trigger(self,data):
        self.trigger = data

    def deal_data(self, conn, addr):
        print ('Accept new connection from {0}'.format(self.addr))
        HELLO = str.encode('Hi, Welcome to the server!')
        self.conn.send(HELLO)
        while 1:
            data = conn.recv(1024)
            self.set_trigger(data)
            print ('{0} client send data is {1}'.format(self.addr, data))
            self.conn.send(str.encode('Hello, {0}'.format(data)))

            if data == EXIT or not data:
                print ('{0} connection close'.format(self.addr))
                BYE = str.encode('Connection closed!')
                self.conn.send(BYE)
                self.conn.close()
                break

        self.conn.close()
