import xadmin
from .models import CommentInfo, KeyWords, SensitiveInfo
from xadmin import views
from xadmin.views.base import CommAdminView
from xadmin.views import ListAdminView
from django.core.paginator import InvalidPage, Paginator


class CommentInfoXadmin():
    list_display = ['title', 'source', 'content', 'mediatype', 'time', 'attribute', 'heat', 'go_to']
    search_fields = ('title', 'content')
    list_filter = ['mediatype', 'source', 'attribute', 'time']
    list_filter = [
        'mediatype', 'source', 'attribute', 'time',
        ("attribute",xadmin.filters.MultiSelectFieldListFilter,),
    ]
    readonly_fields = ['mediatype', 'source', 'attribute', 'time']

    actions_on_top = False
    actions_on_bottom = True
    paginator = Paginator


    date_hierarchy = ['time']
    list_per_page = 50
    list_max_show_all = 200
    ordering = ['-time','-heat']
    empty_value_display = "null"
    #relfield_style = 'fk-ajax'
    refresh_times = [10,30]
    model_icon = 'fa fa-university'
    show_detail_fields=['title']
    list_display_links=['url']
    is_execute = True
    preserve_filters=True

    # list_display=[] #要显示的字段
    # search_fields=[] #搜索的字段
    # list_filter = [] #过滤器
    # date_hierarchy =['publication_date']  #添加过滤（这里是过滤日期）
    # ordering = ['-publication_date',]   #排序（这里以日期排序，加‘-’表示降序）
    # filter_horizontal = ('authors',) #filter_horizontal 从‘多选框’的形式改变为‘过滤器’的方式，水平排列过滤器，必须是一个 ManyToManyField类型，且不能用于 ForeignKey字段，默认地，管理工具使用`` 下拉框`` 来展现`` 外键`` 字段
    # filter_vertical = ['authors',]#同上filter_horizontal，垂直排列过滤器
    # raw_id_fields = ['publisher',] #将ForeignKey字段从‘下拉框’改变为‘文本框’显示
    # list_editable = ['csdevice'] #在列表页可直接编辑的字段
    # model_icon = 'fa fa-user-secret'  #图标样式
    # style_fields = {'csdevice': 'm2m_transfer','csservice': 'ueditor',} #字段显示样式
    # refresh_times = [10, 60] #自动刷新时间
    # show_detail_fields=['ttdsn'] #在指定的字段后添加一个显示数据详情的一个按钮
    # relfield_style = 'fk-ajax' #涉及到外键下拉的时候使用ajax搜索的方式而不是全部列出的方式，比如在分类下拉很多的情况下，这个功能就很好用
    # free_query_filter=['字段1','字段2',......]#默认为 True , 指定是否可以自由搜索. 如果开启自由搜索, 用户可以通过 url 参数来进行特定的搜索
    # exclude=['字段1','字段2',......]#隐藏字段
    # aggregate_fields = {"expire": "max"}#  列聚合，在list表格下面会增加一行统计的数据，可用的值："count","min","max","avg",  "sum"
    # # 添加数据时候，一步一步提供数据，分块显示
    # wizard_form_list = [
    #         ("基础信息", ("name", "contact", "telphone", "address")),
    #         ("其它信息", ("customer_id", "expire", "description")),
    #     ]
    # grid_layouts = ("table", "thumbnails") #列表的布局方式，是以表格一行一条的方式还是类似于缩略图的方式展示的
    # list_per_page = 50 # 每页显示数据的条数
    # list_max_show_all = 200 #每页最大显示数据的条数
    # list_display_links=[] #指定列表显示的哪列可以点击跳转到详情更新页
    # preserve_filters=True #详细页面，删除、修改，更新后跳转回列表后，是否保留原搜索条件
    # save_as = False#详细页面，按钮为“Sava as new” 或 “Sava and add another”
    # save_as_continue = True#点击保存并继续编辑
    # save_on_top = False#详细页面，在页面上方是否也显示保存删除等按钮
    # radio_fields = {"ug": admin.VERTICAL} # 或admin.HORIZONTAL #详细页面时，使用radio显示选项（FK默认使用select）
    # show_full_result_count = True #列表时，模糊搜索后面显示的数据个数样式


class KeyWordsXadmin():
    list_display = ['keyword', 'username', 'status']
    list_filter = ['keyword', 'username', 'status']
    list_per_page = 50
    show_bookmarks = False
    ordering = ['keyword']
    model_icon = 'fa fa-plus-square-o'




class SensitiveXadmin():
    list_display = ['title', 'time', 'source', 'url']
    list_display_links = ['url']
    show_detail_fields = ['title']
    search_fields = ('title', 'source')
    list_filter = ['time', 'title', 'source']
    date_hierarchy = ['time']
    model_icon = 'fa fa-list-alt'
    preserve_filters = True





xadmin.site.register(CommentInfo, CommentInfoXadmin)
xadmin.site.register(KeyWords, KeyWordsXadmin)
xadmin.site.register(SensitiveInfo, SensitiveXadmin)