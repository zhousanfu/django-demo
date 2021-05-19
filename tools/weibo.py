# coding: utf-8

import re
import json
import requests
import os
import time
import pymysql
from datetime import datetime
import sys

# 基于 m.weibo.cn 抓取少量数据，无需登陆验证
url_template = "https://m.weibo.cn/api/container/getIndex?type=wb&queryVal={}&containerid=100103type=2%26q%3D{}&page={}"
keywords = []


def clean_text(text):
    dr = re.compile(r'(<)[^>]+>', re.S)
    dd = dr.sub('', text)
    dr = re.compile(r'#[^#]+#', re.S)
    dd = dr.sub('', dd)
    dr = re.compile(r'@[^ ]+ ', re.S)
    dd = dr.sub('', dd)
    return dd.strip()


def remove_duplication(mblogs):
    mid_set = {mblogs[0]['userid']}
    new_blogs = []
    for blog in mblogs[1:]:
        if blog['userid'] not in mid_set:
            new_blogs.append(blog)
            mid_set.add(blog['userid'])
    return new_blogs


def fetch_pages(query_val, page_num):
    print("微博-", query_val)
    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()
    sqlq = "SELECT keyword FROM database.preception_keywords  WHERE username rlike '去除|不要'"
    cursor.execute(sqlq)
    keyword = cursor.fetchall()
    cursor.close()
    connection.close()
    for i in keyword:
        keywords.append(i[0])

    for page_id in range(page_num - 1):
        try:
            fetch_data(query_val, page_id)
        except Exception as e:
            pass


def fetch_data(query_val, page_id):
    resp = requests.get(url_template.format(query_val, query_val, page_id))
    print(url_template.format(query_val, query_val, page_id))
    card_group = json.loads(resp.text, encoding='utf-8')['data']['cards'][0]['card_group']

    for card in card_group:
        connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
        cursor = connection.cursor()
        
        mblog = card['mblog']


        con = mblog['user']['screen_name']
        url ='https://weibo.com/u/'+str(mblog['user']['id'])+'?is_all=1#'+mblog['id']
        time = datetime.now().strftime("%Y-%m-%d")
        heat = mblog['reposts_count'] + mblog['comments_count'] + mblog['attitudes_count']
        source = query_val
        highpoints = re.compile(u'[\U00010000-\U0010ffff]')
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]') 
        title = highpoints.sub(u'',str(con))
        title = res.sub(u'',con)
        content = clean_text(mblog['text']) #内容

        if any(key in title for key in keywords):
            pass
        else:
            if (len(content) > 5):
                cursor.execute(f'INSERT INTO database.preception_commentinfo(source, title, content, url, time, mediatype, heat) VALUES ("{source}","{title}","{content}","{url}","{time}","微博","{heat}")')
                print(f'INSERT INTO database.preception_commentinfo(source, title, content, url, time, mediatype, heat) VALUES ("{source}","{title}","{content}","{url}","{time}","微博","{heat}")')
                connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    fetch_pages('hello', 200)