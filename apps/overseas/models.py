from django.db import models
from django.utils.safestring import mark_safe

class CommentInfo_India(models.Model):
    source = models.CharField(max_length=20, verbose_name="keywords", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="title", blank=True, null=True)
    content = models.CharField(max_length=5000, verbose_name="content", blank=True, null=True)
    url = models.CharField(max_length=300, verbose_name="URL", blank=True, null=True)
    time = models.DateField(verbose_name="date", blank=True, null=True)
    mediatype = models.CharField(max_length=10, verbose_name="media source", blank=True, null=True)
    attribute = models.CharField(max_length=10, verbose_name="ttributes", blank=True, null=True)
    heat = models.IntegerField(verbose_name="heat", blank=True, null=True)

    def go_to(self):
        return mark_safe('<a href = "'+ self.url +'">Jump</a>')
    go_to.short_description = ""

    class Meta:
        verbose_name = 'Details'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class KeyWords(models.Model):
    keyword = models.CharField(max_length=20, verbose_name='keyword')
    username = models.CharField(max_length=20, verbose_name='operating_name')
    status = models.CharField(max_length=20, verbose_name='crawlign_status')

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = '舆情关键词'
        verbose_name_plural = verbose_name