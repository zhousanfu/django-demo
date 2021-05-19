from django.apps import AppConfig


class SensitiveConfig(AppConfig):
    name = 'sensitive'
    verbose_name = u'SensitiveWord'
    model_icon = 'fa fa-university'
