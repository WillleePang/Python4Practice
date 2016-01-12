#! /usr/bin/env python
# encoding: utf-8


class UrlManager(object):
    def get_shanbay_url(self, shanbay_url, i):
        return shanbay_url + '?page=' + str(i)
