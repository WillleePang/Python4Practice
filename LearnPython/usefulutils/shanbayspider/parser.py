#! /usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse


class Parser(object):
    # shanbay解析器
    '''
    需要解析的html
    <div class="article-item">
        <div class="row">
            <div class="span8">
                <h3 class="article-title">
                    <a href="/footprints/article/7/">笑来寄语——咱是谁？</a>
                </h3>
            </div>
            <div class="span1 pull-right">
                <p class="article-publish-day">22</p>
                <span class="article-publish-month-year">六月, 2012</span>
            </div>
        </div>
        <div class="article-summary">
                <p>不知不觉做事很努力一点，不知不觉更容易坚持原则……于是，许多年后，不知不觉过得比别人好那么一点点。......</p>
        </div>
        <div class="row">
            <div class="span2 pull-right">
                <a class="read-article-link" href="/footprints/article/7/">阅读文章 >></a>
            </div>
        </div>
    </div>
    '''

    def shanbay_parse(self, html, regexp):
        cont_arr = []
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        article_arr = soup.find_all('div', class_='article-item')
        for article in article_arr:
            title = article.find('h3', class_='article-title').get_text()
            if re.findall(regexp, title):
                url = article.find('a', class_='read-article-link')['href']
                cont_arr.append({'title': title, 'url': url})
        return cont_arr

    # 获取最大的页数
    # 需要解析的html
    # <div class="pagination">
    #     <ul>
    #         <li><a class="endless_page_link" href="/footprints/?page=194" rel="page">&lt;&lt;</a></li>
    #         <li><a class="endless_page_link" href="/footprints/" rel="page">1</a></li>
    #         <li><a class="endless_page_link" href="/footprints/?page=2" rel="page">2</a></li>
    #         <li><a class="endless_page_link" href="/footprints/?page=3" rel="page">3</a></li>
    #         <li class="endless_separator"><a href="">...</a></li>
    #         <li><a class="endless_page_link" href="/footprints/?page=193" rel="page">193</a></li>
    #         <li><a class="endless_page_link" href="/footprints/?page=194" rel="page">194</a></li>
    #         <li class="active">
    #         <a class="endless_page_link" href="/footprints/?page=195" rel="page">195</a></li>
    #     </ul>
    # </div>
    def shanbay_get_max_page(self, html):
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        page_arr = soup.find('div', class_='pagination').find_all('a', class_='endless_page_link');
        max_page = page_arr[-2]
        return max_page.get_text()
