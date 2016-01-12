#! /usr/bin/env python
# encoding: utf-8

from usefulutils.shanbayspider import urlmanager, downloader, parser, outputter
import urllib.request
from bs4 import BeautifulSoup
import re
import multiprocessing


# 爬虫的主要控制器
class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = urlmanager.UrlManager()
        # 下载器
        self.downloader = downloader.Downloader()
        # 解析器
        self.parser = parser.Parser()
        # 输出器
        self.outputter = outputter.Outputter()

    # shanbay定向爬虫
    def craw_shanbay(self, shanbay_url, regexp, file_name):
        content = self.downloader.download(shanbay_url)
        max_page = self.parser.shanbay_get_max_page(content)
        for i in range(1, int(max_page) + 1):  #
            try:
                shanbay_new_url = self.urls.get_shanbay_url(shanbay_url, i)
                content = self.downloader.download(shanbay_new_url)
                cont_arr = self.parser.shanbay_parse(content, regexp)
                self.outputter.shanbay_collect_data(cont_arr)
                print('正在爬取shanbay网 no.%d page!' % i)
            except Exception as err:
                print(err)
                print('爬取 failed!')

        self.outputter.shanbay_output_html(file_name)


if __name__ == "__main__":
    spider = SpiderMain()
    shanbay_url = "http://www.shanbay.com/footprints/"
    shanbay_regexp1 = r'地道表达法（第\d+期）'
    name1 = r'地道表达法.htm'
    shanbay_regexp2 = r'读新闻学英语'
    name2 = r'读新闻学英语.htm'
    shanbay_regexp3 = r'【TED推荐】'
    name3 = r'TED推荐.htm'
    shanbay_regexp4 = r'语法教室（第\d+期）'
    name4 = r'语法教室.htm'
    shanbay_regexp5 = r'词根讲解'
    name5 = r'词根讲解.htm'
    shanbay_regexp6 = r'扇贝精读文章'
    name6 = r'扇贝精读文章.htm'
    spider.craw_shanbay(shanbay_url, shanbay_regexp5, name5)

    # test = '\n地道表达法（第107期）\n'
    # if re.findall(r'地道表达法（第\d+期）', test):
    #     print('ok')
    # else:
    #     print('failed')
