import xadmin
from xadmin import views
from xadmin.views.base import CommAdminView
from .views import TestView
from .models import Expensive_Hello
from django.http import HttpResponse
from xadmin.plugins.actions import BaseActionView
from xadmin.plugins import auth
from django.core.paginator import InvalidPage, Paginator


class ClearAction3(BaseActionView):
    '''更改召回action'''
    action_name = "clear_score" 
    description = u'用户-已召回(客服操作)'
    model_perm = 'change' 
    icon = 'fa fa-bug'

    def do_action(self, queryset):
        for obj in queryset:
            obj.status_a = '已召回'
            obj.save()
        msg = "置为‘召回’修改成功 "
        self.message_user(msg, 'success')
        return None


class ClearAction1(BaseActionView):
    '''更改召回action'''
    action_name = "clear_score2" 
    description = u'派发客服(运营操作)'
    model_perm = 'change' 
    icon = 'fa fa-bug'

    def do_action(self, queryset):
        for obj in queryset:
            obj.status_b = '已派发'
            obj.save()
        msg = "置为‘已派发’修改成功 "
        self.message_user(msg, 'success')
        return None


class ClearAction2(BaseActionView):
    '''更改召回action'''
    action_name = "clear_score3" 
    description = u'用户-未召回(客服操作)'
    model_perm = 'change' 
    icon = 'fa fa-bug'

    def do_action(self, queryset):
        for obj in queryset:
            obj.status_a = '未召回'
            obj.save()
        msg = "置为‘未召回’修改成功 "
        self.message_user(msg, 'success')
        return None

class Expensive_Hello_Xadmin():

    list_display = ['day', 'ft', 'aid', 'status_a', 'status_b', 'name','chargetotal', 'punish_type','remark','status','remark_1','ct_2','registertime', 'dlsj', 'chongzhi_30', 'chongzhi_60', 'dlsjs', 'voice_urls']
    search_fields = ['uid', 'aid']
    list_filter = ['day', 'punish_type', 'status_a', 'status_b', 'chargetotal', 'chongzhi_30', 'chongzhi_60']
    filter_horizontal = ['day', 'punish_type', 'status_a', 'status_b', 'chargetotal', 'chongzhi_30', 'chongzhi_60']

    readonly_fields = ['day', 'ft', 'aid', 'name','chargetotal', 'punish_type','remark','status','remark_1','ct_2','registertime', 'dlsj', 'chongzhi_30', 'chongzhi_60', 'dlsjs', 'voice_urls']
    ordering = ['-day', '-chargetotal' ,'chongzhi_60' ,'chongzhi_30']

    relfield_style = 'fk-ajax'
    paginator = Paginator
    date_hierarchy = ['day']
    show_detail_fields=['aid']
    list_display_links=['uid']
    list_per_page = 50

    model_icon = 'fa fa-user-md'

    actions = [ClearAction1, ClearAction2, ClearAction3]
    style_fields = {'csdevice': 'm2m_transfer','csservice': 'ueditor',}


    # 去掉 删除和添加
    def has_delete_permission(self, request=None):
        # Disable delete
        return False

    def has_add_permission(self, request=None):
        # Disable delete
        return False
    
    
    # 数据保存时，将数据关联到用户
    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
    
    # 重写查询方法
    def queryset(self):
        qs = super(Expensive_Hello_Xadmin, self).queryset()
        if self.request.user.last_name == '运营':
            return qs
        elif self.request.user.is_superuser:
            return qs
        else:
            qs_2 = super(Expensive_Hello_Xadmin, self).queryset()
            return qs_2.filter(status_b="已派发")
        try:
            return qs.filter(user=self.request.user)
        except AttributeError:
            return None

    def get_actions(self, request):
        self.actionsactions = super(Expensive_Hello_Xadmin, self).get_actions(request)
        if self.user.last_name != '运营':
            self.actionsactions = [ClearAction1]
        elif self.user.is_superuser:
            self.actionsactions = [ClearAction1, ClearAction2, ClearAction3]
        else:
            self.actionsactions = [ClearAction2, ClearAction3]

        return self.actionsactions


    # def changelist_view(self, request, extra_context=None):
    #     user = request.user
    #     if user.is_superuser:
    #         self.list_display = []
    #     else:
    #         self.list_display = []
    #     return super(Expensive_Hello_Xadmin, self).changelist_view(request, extra_context=None)

    def get_readonly_fields(self):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if self.request.user.last_name == '运营':
            self.readonly_fields = ['status_a']
        elif self.request.user.is_superuser:
            self.readonly_fields = []
        else :
            self.readonly_fields = ['status_b']

        return self.readonly_fields

    def get_list_editable(self):
        if self.request.user.last_name == '运营':
            self.list_editable = ['status_a']
        elif self.request.user.is_superuser:
            self.list_editable = ['status_b', 'status_a']
        else :
            self.list_editable = ['status_b']

        return self.list_editable



xadmin.sites.site.register(Expensive_Hello, Expensive_Hello_Xadmin)
#xadmin.site.register_view(r'chpa/$', TestView, name='chpa')


