# -*- coding: utf-8 -*-

from lxml import etree
import requests
import random
import pymysql
from datetime import datetime
from urllib import parse


def sav_hg():
    #print("香港01")
    UserAgent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3626.109 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.3683.86 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3683.75 Safari/537.36']

    headers = {'User-Agent': random.choices(UserAgent_list)[0]}

    urls = ['https://www.hk01.com/channel/2/%E7%A4%BE%E6%9C%83%E6%96%B0%E8%81%9E',
            'https://www.hk01.com/zone/1/%E6%B8%AF%E8%81%9E',
            'https://www.hk01.com/channel/143/01%E5%81%B5%E6%9F%A5']

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()

    for url in urls:
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            req.encoding='utf-8'
            selector = etree.HTML(req.text)

        infros_title = selector.xpath("//span[@class='jvqc0e-7 fTYKBn s1nfazpo-0 gaLEyK']/a/div/text()")
        infros_url = selector.xpath("//span[@class='jvqc0e-7 fTYKBn s1nfazpo-0 gaLEyK']/a/@href")

        for i in range(len(infros_title)):
            url = parse.unquote(infros_url[i])
            try:
                sql = f'INSERT INTO preception_sensitiveinfo(source, title, url, time) VALUE ("香港01", "{infros_title[i]}", "https://www.hk01.com{url}", "{datetime.now().strftime("%Y-%m-%d")}")'
                cursor.execute(sql)
                connection.commit()
            except pymysql.err.IntegrityError:
                pass
    cursor.close()
    connection.close()


if __name__ == "__main__":
    sav_hg()