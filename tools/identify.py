import pymysql
from snownlp import SnowNLP

#情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
def sentiment(text):
    try:
        if text:
            s1 = SnowNLP(text)
            i1 = s1.sentiments
            return i1
    except ZeroDivisionError:
        i1 = 0
        return i1

def score_identify():
    # 获取链接
    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')

    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            # 查询语句
            sqlq = "SELECT id,title,attribute FROM database.preception_commentinfo WHERE attribute IS NULL;"

            cursor.execute(sqlq)
            resultto = cursor.fetchall()
            
            for ls in resultto:
                sen_score = sentiment(ls[1])
                if sen_score :
                    if sen_score >= 0.85:
                        cursor.execute("UPDATE database.preception_commentinfo SET attribute = '正面' WHERE id = %s;" %(ls[0]))
                    elif sen_score <= 0.45:
                        cursor.execute("UPDATE database.preception_commentinfo SET attribute = '反面' WHERE id = %s;" %(ls[0]))
                    else:
                        cursor.execute("UPDATE database.preception_commentinfo SET attribute = '中立' WHERE id = %s;" %(ls[0]))
                    # 提交
                    connection.commit()
        #关闭指针
        cursor.close()

    finally:
        connection.close()

if __name__ == "__main__":
    score_identify()
