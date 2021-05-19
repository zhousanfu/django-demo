import pymysql
from snownlp import SnowNLP
import jieba
import re
from collections import Counter
import pandas as pd
from datetime import datetime


def frequency():
    day = datetime.now().strftime("%Y-%m-%d")
    
    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()
    sqlq = "SELECT title,content FROM database.preception_commentinfo where time='%s'"%(day)
    cursor.execute(sqlq)
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    df = pd.DataFrame(data)
    df.to_csv('data.txt', sep='\t', index=False)

    cut_words=""
    for line in open('data.txt',encoding='utf-8'):
        line.strip('\n')
        line = re.sub("[\[\【\】\]\,\：\·\—\。\“ \”0-9]", "", line)
        seg_list = jieba.cut(line,cut_all=False)
        cut_words += (" ".join(seg_list))
    all_words = cut_words.split()
    c=Counter()
    for x in all_words:
        if len(x)>1 and x != '\r\n':
            c[x] += 1

    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()

    for (k,v) in c.most_common():
        if v > 3:
            sqlk = "INSERT INTO database.preception_wordsfrequency(word, num, day) VALUES ('{}', '{}', '{}')"
            try:
                cursor.execute(sqlk.format(k, v, day))
            except pymysql.err.InterfaceError:
                connection.ping()
                cursor = connection.cursor()
                cursor.execute(sqlk.format(k, v, day))
            
            connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    frequency()




