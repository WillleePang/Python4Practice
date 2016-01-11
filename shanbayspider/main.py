#! /usr/bin/env python
# encoding: utf-8

from usefulutils.shanbayspider import urlManager, htmlDownloader, htmlParser, htmlOutputer


class SpiderMain(object):
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.downloader = htmlDownloader.Downloader()
        self.parser = htmlParser.Parser()
        self.outputer = htmlOutputer.Outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.hasNewUrl():
            try:
                new_url = self.urls.getNewUrl()
                print('craw %d : %s' % (count, new_url))
                content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, content)
                self.urls.addNewUrls(new_url)
                self.outputer.collectData(new_data)

                if count == 1000:
                    break

                count += 1
            except:
                print('craw failed!');


if __name__ == "__main__":
    root_url = ""
    spider = SpiderMain()
    spider.craw(root_url)
