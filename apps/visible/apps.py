from django.apps import AppConfig


class VisibleConfig(AppConfig):
    name = 'visible'
    verbose_name = u'Hello用户管理'
    model_icon = 'fa fa-puzzle-piece'