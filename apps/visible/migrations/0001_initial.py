# Generated by Django 2.0 on 2020-10-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expensive_Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(blank=True, null=True, verbose_name='封禁日期')),
                ('post_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='流水号')),
                ('aid', models.CharField(blank=True, max_length=20, null=True, verbose_name='用户ID')),
                ('uid', models.CharField(blank=True, max_length=20, null=True, verbose_name='用户UID')),
                ('nickname', models.CharField(blank=True, max_length=255, null=True, verbose_name='昵称')),
                ('chargetotal', models.IntegerField(blank=True, null=True, verbose_name='累计充值(钻石)')),
                ('roomtype', models.CharField(blank=True, max_length=255, null=True, verbose_name='房间类型')),
                ('usernum', models.IntegerField(blank=True, null=True, verbose_name='房间人气')),
                ('high_score', models.IntegerField(blank=True, null=True, verbose_name='高危积分')),
                ('report_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='举报原因')),
                ('operator_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='审核人')),
                ('ct', models.DateTimeField(blank=True, null=True, verbose_name='工单生成时间')),
                ('ft', models.DateTimeField(blank=True, null=True, verbose_name='审核时间')),
                ('business', models.CharField(blank=True, max_length=255, null=True, verbose_name='业务')),
                ('atype', models.CharField(blank=True, max_length=255, null=True, verbose_name='业务类型')),
                ('source', models.CharField(blank=True, max_length=255, null=True, verbose_name='业务来源')),
                ('punish_type', models.CharField(blank=True, choices=[('正常', '正常'), ('账号封禁', '账号封禁')], max_length=255, null=True, verbose_name='账号状态')),
                ('remark', models.CharField(blank=True, max_length=255, null=True, verbose_name='处罚原因')),
                ('voice_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='url')),
                ('voice_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='语音文本')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='内容')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='是否手动解封')),
                ('remark_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='解封备注')),
                ('ct_2', models.DateTimeField(blank=True, null=True, verbose_name='解封时间')),
                ('guild_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='公会ID')),
                ('igt', models.DateTimeField(blank=True, null=True, verbose_name='入会时间')),
                ('member_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='等级')),
                ('creator_uid', models.IntegerField(blank=True, null=True, verbose_name='公会创建用户uid')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='公会名')),
                ('signature', models.CharField(blank=True, max_length=255, null=True, verbose_name='公会个签')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='公会描述')),
                ('registertime', models.DateField(blank=True, null=True, verbose_name='注册日期')),
                ('user_name_uc', models.CharField(blank=True, max_length=255, null=True, verbose_name='注册方式')),
                ('dlsj', models.DateTimeField(blank=True, null=True, verbose_name='最近登录时间')),
                ('chongzhi_30', models.IntegerField(blank=True, null=True, verbose_name='近30天充值(钻石)')),
                ('chongzhi_60', models.IntegerField(blank=True, null=True, verbose_name='近60天充值(钻石)')),
                ('status_a', models.CharField(blank=True, choices=[('未召回', '未召回'), ('已召回', '已召回')], default='未召回', max_length=255, verbose_name='召回情况')),
                ('status_b', models.CharField(blank=True, choices=[('未派发', '未派发'), ('已派发', '已派发')], default='未派发', max_length=255, verbose_name='派发给客服')),
            ],
            options={
                'verbose_name': 'Hello用户召回',
                'verbose_name_plural': 'Hello用户召回',
            },
        ),
    ]
