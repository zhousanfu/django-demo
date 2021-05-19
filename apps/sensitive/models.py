from django.db import models
from django.utils.safestring import mark_safe

class Word_Accuracy(models.Model):
    date = models.DateField(verbose_name="日期", blank=True, null=True)
    #(max_length=20, verbose_name="keywords", blank=True, null=True)
    word_id = models.CharField(max_length=50, verbose_name="敏感词ID", blank=True, null=True)
    content = models.CharField(max_length=10000, verbose_name="敏感词内容", blank=True, null=True)
    countrys = models.CharField(max_length=20, verbose_name="国家码", blank=True, null=True)
    level = models.CharField(max_length=20, verbose_name="等级", blank=True, null=True)
    remark = models.CharField(max_length=255, verbose_name="备注", blank=True, null=True)
    stype = models.CharField(max_length=20, verbose_name="词类型", blank=True, null=True)
    sensitive_type = models.CharField(max_length=20, verbose_name="违规类型", blank=True, null=True)
    status = models.CharField(max_length=20, verbose_name="状态", blank=True, null=True)
    source = models.CharField(max_length=20, verbose_name="质检来源", blank=True, null=True)
    cnt7 = models.IntegerField(max_length=11, verbose_name="过去7天质检量", blank=True, null=True)
    accuracy7 = models.FloatField(verbose_name="7天准确率", blank=True, null=True)
    cnt30 = models.IntegerField(max_length=11, verbose_name="过去30天质检量", blank=True, null=True)
    accuracy30 = models.FloatField(verbose_name="30天准确率", blank=True, null=True)

    # def go_to(self):
    #     return mark_safe('<a href = "'+ self.url +'">Jump</a>')
    # go_to.short_description = ""

    class Meta:
        verbose_name = 'accuracy'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.word_id