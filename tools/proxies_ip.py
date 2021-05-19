#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import lxml.html
import os
import time


#https://ip.ihuan.me/address/576O5Zu9.html?page=

class Proxies_Ip(object):

    def __init__(self, url):
        self.__url = url
        self.__headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            }
        self.__ip = []


    def get_ihuanip(self):
        content = requests.get(self.__url, self.__headers)
        if content.status_code == 200:
            content.encoding='utf-8'
            selector = etree.HTML(content.text)
            content_ip = selector.xpath("//table[@class='table table-hover table-bordered']/tbody/tr/td[1]/a/text()")
            content_host = selector.xpath("//table[@class='table table-hover table-bordered']/tbody/tr/td[2]/text()")


            for i in range(min(len(content_ip), len(content_host)) ):
                self.__ip.append(content_ip[i] + ':' + content_host[i])

        return self.__ip