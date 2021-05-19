import pymysql
from multiprocessing import Pool
import schedule, time
from tools.weibo import fetch_pages
from tools.identify import score_identify
from tools.word_frequency import frequency
from tools.hive_presto import get_presto_hiveSql
from tools.baidu import get_content
from tools.toutiao import touttiao
from tools.bannedbook import sav_hg
from tools.overseas import sav_ndtv, sav_timesofindia
import os, sys
import functools


def catch_exceptions(job_func, cancel_on_failure=False):
    @functools.wraps(job_func)
    def wrapper(*args, **kwargs):
        try:
            return job_func(*args, **kwargs)
        except:
            import traceback
            print(traceback.format_exc())
            if cancel_on_failure:
                return schedule.CancelJob
    return wrapper

def run_my_tools():
    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    sql_deleteurl = "DELETE FROM database.preception_commentinfo WHERE Id NOT IN (SELECT Id FROM (SELECT MIN(Id) AS Id FROM database.preception_commentinfo GROUP BY url) t)"
    sql_delmix = "DELETE FROM database.preception_commentinfo WHERE LENGTH(content)<=5"
    cursor = connection.cursor()
    cursor.execute(sql_deleteurl)
    connection.commit()
    cursor.execute(sql_delmix)
    print('去重1', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    connection.commit()
    cursor.close()
    connection.close()

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()
    sqlq = "SELECT keyword FROM database.preception_keywords WHERE username NOT RLIKE '去除|不要'"
    cursor.execute(sqlq)
    keyword = cursor.fetchall()
    cursor.close()
    connection.close()

    try:
        sav_hg()
    except:
        print("sav_hg爬取错误-" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    try:
        pool = Pool(processes=10)
        for i in range(len(keyword)):
            pool.apply_async(get_content, args=(keyword[i][0], 200))
        pool.close()
        pool.join()
    except:
        print("get_content爬取错误-" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    try:
        pool = Pool(processes=10)
        for i2 in range(len(keyword)):
            pool.apply_async(fetch_pages, args=(keyword[i2][0], 200))
        pool.close()
        pool.join()
    except:
        print("fetch_pages爬取错误-" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    try:
        for i3 in range(len(keyword)):
            touttiao(keyword[i3][0])
    except:
        print("touttiao爬取错误-" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    score_identify()
    #frequency()

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    sql_deleteurl = "DELETE FROM database.overseas_commentinfo_india WHERE Id NOT IN (SELECT Id FROM (SELECT MIN(Id) AS Id FROM database.overseas_commentinfo_india GROUP BY url) t)"
    #slq_deltime = "DELETE FROM database.preception_commentinfo WHERE DATE(`time`) <= DATE_SUB(CURDATE(), INTERVAL 10 DAY)"
    #sql_sensitive = "DELETE FROM database.preception_sensitiveinfo WHERE Id NOT IN (SELECT Id FROM (SELECT MIN(Id) AS Id FROM database.preception_sensitiveinfo GROUP BY title) t)"
    cursor = connection.cursor()
    cursor.execute(sql_deleteurl)
    connection.commit()
    print('去重1', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    cursor.close()
    connection.close()

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()
    sqlq = "SELECT keyword FROM database.overseas_keywords"
    cursor.execute(sqlq)
    keyword = cursor.fetchall()
    cursor.close()
    connection.close()

    for i2 in range(len(keyword)):
        try:
            print(keyword[i2][0])
            sav_timesofindia(keyword[i2][0])
            sav_ndtv(keyword[i2][0])
        except:
            print("sav_timesofindia爬取错误-" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print("sav_mysql")

    os.system('cls')
    print("爬取完毕-" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def run():
    schedule.every(60).minutes.do(run_my_tools)
    #schedule.every().hour.do(run_my_tools)
    #schedule.every().day.at("09:25").do(set_mysql)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run()