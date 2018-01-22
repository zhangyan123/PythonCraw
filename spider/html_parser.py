#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import urllib
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self):
        pass

    def _get_new_urls(self,page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'/item/'))
        for link in links :
            new_url = link['href']
            new_full_url = urllib.parse.urljoin('https://baike.baidu.com',new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url, soup):
        res_data = {}
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        res_data['url'] = page_url
        description_node = soup.find('div',class_ = 'lemma-summary').find('div',class_ = 'para')
        res_data['description'] = description_node.get_text()
        # print(description_node.get_text())
        return res_data   


    def parse(self,page_url, html_count):
        if page_url is None or html_count is None:
            return
        soup  = BeautifulSoup(html_count, 'html.parser', from_encoding = 'utf-8')
        if soup is None:
            return
        else:
            
            new_urls = self._get_new_urls(page_url, soup)
            new_data = self._get_new_data(page_url, soup)
            return new_urls, new_data