# -*- coding: utf-8 -*-

from lxml import etree
import requests
from requests.packages import urllib3
import logging
import random, time, re, os
import pymysql
from datetime import datetime
from tools.proxies_ip import Proxies_Ip


def sav_timesofindia(keyword):

    pi = Proxies_Ip('https://ip.ihuan.me')
    ip_list = pi.get_ihuanip()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'text/css; charset=utf-8'}
    url = 'https://timesofindia.indiatimes.com/topic/'+keyword+'/news'
    requests.packages.urllib3.disable_warnings()

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()

    for ip in ip_list:
        print(ip)
        try:
            req = requests.get(url, headers=headers, proxies={"http": f"http://{ip}", "https": f"https://{ip}"}, verify=False, timeout=60)
        except requests.RequestException:
            print("不可用")
            continue

        if req.status_code == 200:
            req.encoding='utf-8'
            selector = etree.HTML(req.text)
            infros_title = selector.xpath("//div[@class='tab_content']/ul/li[@class='article']/div[@class='content']/a/span[@class='title']/text()")
            infros_content = selector.xpath("//div[@class='tab_content']/ul/li[@class='article']/div[@class='content']/a/p/text()")
            infros_url = selector.xpath('//*[@id="c_topic_list1_1"]/div/ul/li/div/a/@href')
            print(infros_title[0])

            for i in range(min(len(infros_title), len(infros_content), len(infros_url)) ):
                sql = "INSERT INTO overseas_commentinfo_india (country,source,title,content,url,time,mediatype) VALUES ('india',%s,%s,%s,%s,%s,'timesofindia')"
                cursor.execute(sql,(keyword,infros_title[i],infros_content[i],"https://timesofindia.indiatimes.com"+infros_url[i],datetime.now().strftime("%Y-%m-%d")) )
                connection.commit()
            break

    cursor.close()
    connection.close()


def sav_ndtv(keyword):
    pi = Proxies_Ip('https://ip.ihuan.me')
    ip_list = pi.get_ihuanip()
    
    useragent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3626.109 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.3683.86 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3683.75 Safari/537.36']
    headers = {'User-Agent': random.choices(useragent_list)[0]}
    url = 'https://www.ndtv.com/search?searchtext='+keyword

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()

    for ip in ip_list:
        try:
            req = requests.get(url, headers=headers, proxies={"http": f"http://{ip}", "https": f"https://{ip}"}, verify=False, timeout=60)
        except requests.RequestException:
            print("不可用")
            continue
        
        if req.status_code == 200:
            req.encoding='utf-8'
            selector = etree.HTML(req.text)
            infros_title = selector.xpath("//div[@id='news_list']/div[2]/ul/li/p[@class='header fbld']/a/strong/text()")
            time_list = selector.xpath("//div[@id='news_list']/div[2]/ul/li/p[@class='list_dateline']/text()")
            type_list = selector.xpath("//div[@id='news_list']/div[2]/ul/li/p[@class='list_dateline']/a/font/font/text()")
            infros_content = selector.xpath("//div[@id='news_list']/div[2]/ul/li/p[@class='intro']/font/font/text()")
            infros_url = selector.xpath("//div[@id='news_list']/div[2]/ul/li/p[@class='header fbld']/a/@href")

            for i in range(len(infros_title), len(time_list), len(type_list), len(infros_content), len(infros_url)):
                sql = 'INSERT INTO overseas_commentinfo_india (country, source, title, content, url, time, mediatype) VALUES ("india","{}","{}","{}","{}","{}","ndtv")'
                cursor.execute(sql, (format(keyword, infros_title[i], infros_content[i], "https://www.ndtv.com/"+infros_url[i], datetime.now().strftime("%Y-%m-%d"))) )
                connection.commit()
            break

    cursor.close()
    connection.close()


if __name__ == "__main__":
    sav_timesofindia('hello')