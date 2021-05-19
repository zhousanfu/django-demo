from django.db import models
from django.utils.safestring import mark_safe
from xadmin.plugins.actions import BaseActionView
from datetime import datetime
from django.utils import timezone


class Expensive_Hello(models.Model):

    status_a = (('未召回','未召回'),('已召回','已召回'))
    status_b = (('未派发','未派发'),('已派发','已派发'))
    punish_type = (('正常','正常'),('账号封禁','账号封禁'))

    day  = models.DateField(verbose_name="封禁日期", blank=True, null=True)
    post_id  = models.CharField(verbose_name="流水号", blank=True, null=True, max_length=255)
    aid = models.CharField(verbose_name="用户ID", blank=True, null=True, max_length=20)
    uid = models.CharField(verbose_name="用户UID", blank=True, null=True, max_length=20)
    nickname  = models.CharField(verbose_name="昵称", blank=True, null=True, max_length=255)
    chargetotal = models.IntegerField(verbose_name="累计充值(钻石)", blank=True, null=True)
    roomtype  = models.CharField(verbose_name="房间类型", blank=True, null=True, max_length=255)
    usernum = models.IntegerField(verbose_name="房间人气", blank=True, null=True)
    high_score = models.IntegerField(verbose_name="高危积分", blank=True, null=True)
    report_desc  = models.CharField(verbose_name="举报原因", blank=True, null=True, max_length=255)
    operator_name  = models.CharField(verbose_name="审核人", blank=True, null=True, max_length=255)
    ct  = models.DateTimeField(verbose_name="工单生成时间", blank=True, null=True,)
    ft  = models.DateTimeField(verbose_name="审核时间", blank=True, null=True,)
    business  = models.CharField(verbose_name="业务", blank=True, null=True, max_length=255)
    atype  = models.CharField(verbose_name="业务类型", blank=True, null=True, max_length=255)
    source  = models.CharField(verbose_name="业务来源", blank=True, null=True, max_length=255)
    punish_type  = models.CharField(choices=punish_type, verbose_name="账号状态", blank=True, null=True, max_length=255)
    remark  = models.CharField(verbose_name="处罚原因", blank=True, null=True, max_length=255)
    voice_url  = models.CharField(verbose_name="url", blank=True, null=True, max_length=255)
    voice_text  = models.CharField(verbose_name="语音文本",blank=True, null=True, max_length=255)
    content = models.CharField(verbose_name="内容",blank=True, null=True, max_length=255)
    status = models.CharField(verbose_name="是否手动解封",blank=True, null=True, max_length=255)
    remark_1 = models.CharField(verbose_name="解封备注",blank=True, null=True, max_length=255)
    ct_2 = models.DateTimeField(verbose_name="解封时间", blank=True, null=True,)
    guild_id = models.CharField(verbose_name="公会ID", blank=True, null=True, max_length=255)
    igt  = models.DateTimeField(verbose_name="入会时间", blank=True, null=True,)
    member_type  = models.CharField(verbose_name="等级",blank=True, null=True, max_length=255)
    creator_uid = models.IntegerField(verbose_name="公会创建用户uid", blank=True, null=True)
    name  = models.CharField(verbose_name="公会名",blank=True, null=True, max_length=255)
    signature  = models.CharField(verbose_name="公会个签",blank=True, null=True, max_length=255)
    description  = models.CharField(verbose_name="公会描述",blank=True, null=True, max_length=255)
    registertime  = models.DateField(verbose_name="注册日期", blank=True, null=True)
    user_name_uc  = models.CharField(verbose_name="注册方式",blank=True, null=True, max_length=255)
    dlsj  = models.DateTimeField(verbose_name="最近登录时间", blank=True, null=True,)
    chongzhi_30 = models.IntegerField(verbose_name="近30天充值(钻石)", blank=True, null=True)
    chongzhi_60 = models.IntegerField(verbose_name="近60天充值(钻石)", blank=True, null=True)
    status_a  = models.CharField(choices=status_a, verbose_name="召回情况", blank=True, default="未召回", max_length=255)
    status_b = models.CharField(choices=status_b, verbose_name="派发给客服", blank=True, default="未派发", max_length=255)




    #<audio controls="controls" controlslist="nodownload" src="http://gdl.ppx520.com/cn/vio-music/1c2/007KXa.wav?User=BigoAudit&amp;"></audio>
    def voice_urls(self):
        return mark_safe('<audio controls="controls" controlslist="nodownload" src="'+ str(self.voice_url) +'"></audio>')

    # def status_as(self):
    #     return mark_safe('<select type="text" name="form-2-status_a" id="id_form-2-status_a" class="vTextField">\
    #         <option value ="PUDH召回">PUDH召回</option>\
    #         <option value ="电话召回">电话召回</option>\
    #         <option value="短信召回">短信召回</option>\
    #         <option value="否" selected="select">' + self.status_a + '</option></select>')


    def dlsjs(self):
        #cday = datetime.strptime(self.dlsj, '%Y-%m-%d %H:%M:%S')
        if self.dlsj:
            slsjs = (timezone.now() - self.dlsj).days
            return mark_safe(slsjs)
    dlsjs.short_description = "离开天数"
        

    def get_chargetotal(self):
        entry = Expensive_Hello.objects.filter(chargetotal__gt = 1)
        return entry

    class Meta:
        verbose_name = 'Hello用户召回'
        verbose_name_plural = verbose_name

    
    def __str__(self):
        return self.nickname

