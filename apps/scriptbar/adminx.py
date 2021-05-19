import xadmin
from xadmin import views
from .views import Scriptbar, Json_to_excel


class GlobalSetting(object):  #名称不能改
    def get_site_menu(self):
        return [
            {
                'title': '脚本工具',
                'icon': 'fa fa-puzzle-piece',       # Font Awesome图标
                'menus':(
                    {
                        'title': '文本拦截查询',
                        'icon': 'fa fa-file-word-o',
                        'url': '/scriptbar/'
                        
                    },
                    {
                        'title': 'json转excel',
                        'icon': 'fa fa-file-excel-o',
                        'url': '/json_to_excel/',
                    }
                )
            },
        ]


xadmin.site.register_view(r'scriptbar/$', Scriptbar, name='Scriptbar')
xadmin.site.register_view(r'json_to_excel/$', Json_to_excel, name='Json_to_excel')
xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
