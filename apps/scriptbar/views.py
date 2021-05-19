from django.shortcuts import render
from xadmin.views import CommAdminView
from tools import hive_presto
import time
import pymysql



# Create your views here.
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

class BarView(CommAdminView):
    def get(self, request):
        context = super().get_context()     # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        title = "脚本工具"     #定义面包屑变量
        context["breadcrumbs"].append({'url': 'xadmin/script_bar/', 'title': title})   #把面包屑变量添加到context里面
        context["title"] = title   #把面包屑变量添加到context里面

        uid = request.GET.get('uid','')
        con = request.GET.get('con','')
        day1 = request.GET.get('day1','')
        day2 = request.GET.get('day2','')
        bus = request.GET.get('bus', '')

        if uid and day1 and day2:
            sql = "SELECT rtime,app_id,uid,content,word_id,keyword,country\nfrom bigolive.bigo_keyword_match_info\nWHERE day>='{}' \nAND day<='{}' \nAND uid={} \nORDER BY day DESC"
            sql = sql.format(day1,day2,uid)
            if bus:
                sql = "SELECT rtime,app_id,uid,content,word_id,keyword,country\nfrom bigolive.bigo_keyword_match_info\nWHERE day>='{}' \nAND day<='{}' \nAND uid={} \nAND business_id={} \nORDER BY day DESC"
                sql = sql.format(day1,day2,uid,bus)
                context["intercept_data"] = hive_presto.get_presto_hiveSql(sql)
            else:
                context["intercept_data"] = hive_presto.get_presto_hiveSql(sql)


        if con and day1 and day2:
            sql = "SELECT rtime,app_id,uid,content,word_id,keyword,country\nfrom bigolive.bigo_keyword_match_info\nWHERE day>='{}' \nAND day<='{}' \nAND content rlike '{}' \nORDER BY day"
            sql = sql.format(day1,day2,con)
            if bus:
                sql = "SELECT rtime,app_id,uid,content,word_id,keyword,country\nfrom bigolive.bigo_keyword_match_info\nWHERE day>='{}' \nAND day<='{}' \nAND content rlike '{}' \nAND business_id={} \nORDER BY day DESC"
                sql = sql.format(day1,day2,con,bus)
                context["intercept_data"] = hive_presto.get_presto_hiveSql(sql)
            else:
                context["intercept_data"] = hive_presto.get_presto_hiveSql(sql)

        return render(request, 'scriptbar.html', context)



class Scriptbar(CommAdminView):
    def get(self, request):
        context = super().get_context()     # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "脚本工具"     #定义面包屑变量
        context["breadcrumbs"].append({'url': '/scriptbar/', 'title': title})   #把面包屑变量添加到context里面
        context["title"] = title   #把面包屑变量添加到context里面

        return render(request, 'scriptbar.html', context)   #最后指定自定义的template模板，并返回context

#json_to_excel
class Json_to_excel(CommAdminView):
    def get(self, request):
        context = super().get_context()     # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "json_to_excel"     #定义面包屑变量
        context["breadcrumbs"].append({'url': '/json_to_excel/', 'title': title})   #把面包屑变量添加到context里面
        context["title"] = title   #把面包屑变量添加到context里面

        return render(request, 'json_to_excel.html', context)   #最后指定自定义的template模板，并返回context