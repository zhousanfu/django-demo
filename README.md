# 基于Djanog网络舆情监测 Digital monitoring
> 本项目使用djanog,后台界面管理


# 一、django指定
 python3 manage.py runserver 0.0.0.0:8324
 1, django 创建   django-admin startproject project_name
 2, django 建app  python manage.py startapp app_name
 3, 创建超级用户    python py
 数据查询/迁移/同步
 python manage.py makemigrations
 python manage.py migrate
 

# 二、特定模块，python3.7
python3 -m pip install mysqlclient==1.3.13


# 三、爬虫scrapy
```
>  scrapy startproject douban_demo
>  scrapy crawl tencent
>  douban_demo
>  ├── douban_demo
>  |   |   spiders        # 放置spider代码的目录;（编写爬取网站规则）
>  │   ├── items.py       # 项目中的item文件;（定义结构化数据字段field）.
>  │   ├── middlewares.py # 中间件文件，配置所有中间件 
>  │   ├── pipelines.py   # 项目中的pipelines文件;（用于存放执行后期数据处理的功能，定义如何存储结构化数据)
>  │   ├── settings.py    # 项目的设置文件；(如何修改User-Agent，设置爬取时间间隔，设置代理，配置中间件等等)
>  │   └── spiders        # Spider类文件夹，所有的Spider均在此存放
>  └── scrapy.cfg         # 整个Scrapy的配置文件，由Scrapy自动生成
>  ```
## twitter接口 url = "https://twitter.com/search?q=两会&src=typed_query/"



