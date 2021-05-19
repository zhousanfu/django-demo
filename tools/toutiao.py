# 导入所需的库
import requests
import json
import pandas as pd
import time
import random
from datetime import datetime
import pymysql
 

def touttiao(keyword):
	print("头条-", keyword)
	connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
	cursor = connection.cursor()

	UserAgent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
						'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
						'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36']
	Cookie = 'tt_webid=6741334664763835907; WEATHER_CITY=%E5%8C%97%E4%BA%AC; ' \
				'tt_webid=6741334664763835907; csrftoken=af5535d3c7e019b988ec0f93b7f1774d; ' \
				's_v_web_id=9985dd97ccfd39b145674d0955a295a1; ' \
				'__tasessionId=pj925vib61569648686929'

	headers = {
		'User-Agent': random.choices(UserAgent_list)[0],  # 使用random模块中的choices()方法随机从列表中提取出一个内容
		'Cookie': Cookie
	}

	url = f'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword={keyword}&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'

	response = requests.get(url=url, headers=headers)
	if response.status_code == 200:
		json_data = response.text
		dict_data = json.loads(json_data, encoding='utf-8')
		news_data = dict_data['data']

	for i in range(len(news_data)):

		try:
			title = news_data[i]['title']
		except :
			title = ''

		try:
			abstract = news_data[i]['abstract']
		except :
			abstract = ''


		try:
			article_url = news_data[i]['article_url']
		except KeyError:
			article_url = 'NULL'

		try:
			read_count = news_data[i]['read_count']
		except KeyError:
			read_count = 0

		try:
			comment_count = news_data[i]['comment_count']
		except KeyError:
			comment_count = 0

		time = datetime.now().strftime("%Y-%m-%d")

		count = read_count + comment_count

		if len(title) >= 5: 
			sql = f'INSERT INTO preception_commentinfo(source, title, content, url, time, mediatype, heat) VALUE ("{keyword}", "{title}", "{abstract}", "{article_url}", "{time}", "今日头条", "{count}")'
			print(sql)
			cursor.execute(sql)
			connection.commit()
	cursor.close()
	connection.close()

if __name__ == "__main__":
	touttiao("网络直播")