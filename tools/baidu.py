#!/usr/bin/python3
# -*- coding: utf-8 -*-
import codecs
import importlib
import os
import re
import shutil
import sys
import time
import json
import pymysql
import chardet
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import lxml.html
import random


BASE_URL = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "referer": "https://www.baidu.com/"
        }



def get_content(kw, max_pn):
    print("百度-", kw)

    url_list = [BASE_URL.format(kw, pn) for pn in range(0, max_pn, 50)]
    hrefs_id = []
    for url in url_list:
        #print(url)
        try:
            response = requests.get(url=url, headers=HEADERS)
            hrefs = re.findall('(?<=<a rel="noreferrer" href="/p/).{0,10}', response.text)
            for i in range(len(hrefs)):
                a = hrefs.pop()
                hrefs_id.append(a)
        except:
            continue

    #print(hrefs_id)
        

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()

    hrefs_id = list(set(hrefs_id))

    for lin in hrefs_id:
        response = requests.get('https://tieba.baidu.com/p/{}'.format(lin), headers=HEADERS)
        soup = BeautifulSoup(response.text)
        try:
            batitle = soup.h1['title']
        except TypeError:
            batitle = soup.h3['title']
        batitle = re.sub(u'[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]|[\n\'\"]','',batitle)
        heat = soup.select('.red')[0].text
        speak = soup.findAll("div", {"id":re.compile("post_content_.*?")})
        content = []
        for i in speak:
            itext = re.sub(u'[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]|[\n\'\"]','',i.text)
            content.append(itext.lstrip())
        tieba_url = 'https://tieba.baidu.com/p/'+lin
        time = datetime.now().strftime("%Y-%m-%d")

        sql = 'INSERT INTO database.preception_commentinfo(source, title, content, url, time, mediatype, heat) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'
        sql = sql.format(kw, batitle, content, tieba_url, time, '百度贴吧', heat)

        try:
            cursor.execute(sql)
        except pymysql.err.DataError:
            sql = 'INSERT INTO database.preception_commentinfo(source, title, content, url, time, mediatype, heat) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'
            content = content[:200]
            sql = sql.format(kw, batitle, content, tieba_url, time, '百度贴吧', heat)
        connection.commit()


    cursor.close()
    connection.close()


if __name__ == '__main__':
    get_content("hello", 200)
    #a = get_proxies()