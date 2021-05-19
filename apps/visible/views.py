from django.shortcuts import render
import pymysql
from xadmin.views import CommAdminView
from django.http import HttpResponse
import pandas as pd



def sqlparse(context):
    sql = "Select * from %s Where PERIOD = '%s' And UNIT = '%s'" % \
          (DB_TABLE, context['period_selected'], context['unit_selected']) # context为前端通过表单传来的字典
    # sql = sql_extent(sql, '[TC I]', context['tc_i_selected']) #未来可以通过进一步拼接字符串动态扩展sql语句
    return sql

def index(request):
    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT count(*) FROM database.intercept"
    df = pd.read_sql_query(sql, connection)
    context = {'data':df}
    cursor.close()
    connection.close()

    return render(request, 'visible_index.html', context)


def get_mysql(sql):
    data_dict = object
    connection = pymysql.connect(host='host',port=3306,user='root',password='pass',db='database',charset='utf8mb4')
    cursor = connection.cursor()
    
    try:
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
    except:
        connection.rollback()
    #data = cursor.fetchall()
    #connection.commit()
    cursor.close()
    connection.close()

    return data_dict


# Create your views here.
class TestView(CommAdminView):
    def get(self, request):
        context = super().get_context()
        title = "数据可视化"
        context["breadcrumbs"].append({'url': '/intercept/', 'title': title})
        context["title"] = title


        app = request.GET.get('app','')
        bus = request.GET.get('bus','')

        sql = "SELECT a.app_id,group_concat(a.date) as date,group_concat(a.num)as number\
            FROM(SELECT app_id,`date`,SUM(number) as num\
            FROM database.intercept\
            WHERE `date`<date_format(now(),'%y-%m-%d')\
            AND `date`>=DATE_SUB(date_format(now(),'%y-%m-%d'),INTERVAL 7 DAY)"

        if app:
            app = "and app_id=" + str(app)
            sql = sql + '\t'+app+'\t'


        if bus:
            bus = "and business_id=" + str(bus)
            sql = sql + '\t'+bus+'\t'

        sql = sql + "GROUP BY app_id,date ORDER BY app_id,date)a GROUP BY a.app_id"

        data = get_mysql(sql)

        try:
            for i in data:
                date_str = i['date']
                number_str = i['number']
                i['date'] = date_str.split(',',)
                i['number'] = number_str.split(',',)

            context['option'] = data
        except:
            pass

        return render(request, 'visible_echarts.html', context)




