#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import ssl

class HtmlDownloader(object):
    def __init__(self):
        pass
    def download(self,url):
        context = ssl._create_unverified_context()
        if url is None:
            return
        response = urllib.request.urlopen(url,context=context)
        if response.getcode() != 200:
            return

        else:
            return response.read()