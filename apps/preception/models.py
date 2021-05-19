from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class CommentInfo(models.Model):
    source = models.CharField(max_length=10, verbose_name="关键词", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="标题", blank=True, null=True)
    url = models.CharField(max_length=300, verbose_name="链接", blank=True, null=True)
    attribute = models.CharField(max_length=10, verbose_name="舆情属性", blank=True, null=True)
    mediatype = models.CharField(max_length=10, verbose_name="媒体来源", blank=True, null=True)
    time = models.DateField(verbose_name="日期", blank=True, null=True)
    heat = models.IntegerField(verbose_name="热度", blank=True, null=True)
    content = models.CharField(max_length=5000, verbose_name="内容", blank=True, null=True)

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<a href = "'+ self.url +'">跳转</a>')
    go_to.short_description = "跳转"

    class Meta:
        verbose_name = '舆情详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



class KeyWords(models.Model):
    keyword = models.CharField(max_length=20, verbose_name='关键词')
    username = models.CharField(max_length=20, verbose_name='用户名')
    status = models.CharField(max_length=20, verbose_name='状态')

    class Meta:
        verbose_name = '舆情关键词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keyword


# class WordsFrequency(models.Model):
#     word = models.CharField(max_length=255, verbose_name="词")
#     num = models.IntegerField(verbose_name="词频")
#     day = models.CharField(max_length=255, verbose_name="日期")

#     def __str__(self):
#         return self.word

#     class Meta:
#         verbose_name = '词频统计'
#         verbose_name_plural = verbose_name


class SensitiveInfo(models.Model):
    source = models.CharField(max_length=10, verbose_name="来源", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="标题", blank=True, null=True)
    url = models.CharField(max_length=300, verbose_name="链接", blank=True, null=True)
    time = models.DateField(verbose_name="日期", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '敏感新闻'
        verbose_name_plural = verbose_name
