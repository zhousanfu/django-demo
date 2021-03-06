# Generated by Django 2.0 on 2020-10-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=10, null=True, verbose_name='关键词')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='标题')),
                ('url', models.CharField(blank=True, max_length=300, null=True, verbose_name='链接')),
                ('attribute', models.CharField(blank=True, max_length=10, null=True, verbose_name='舆情属性')),
                ('mediatype', models.CharField(blank=True, max_length=10, null=True, verbose_name='媒体来源')),
                ('time', models.DateField(blank=True, null=True, verbose_name='日期')),
                ('heat', models.IntegerField(blank=True, null=True, verbose_name='热度')),
                ('content', models.CharField(blank=True, max_length=5000, null=True, verbose_name='内容')),
            ],
            options={
                'verbose_name': '舆情详情',
                'verbose_name_plural': '舆情详情',
            },
        ),
        migrations.CreateModel(
            name='KeyWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20, verbose_name='关键词')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('status', models.CharField(max_length=20, verbose_name='状态')),
            ],
            options={
                'verbose_name': '舆情关键词',
                'verbose_name_plural': '舆情关键词',
            },
        ),
        migrations.CreateModel(
            name='SensitiveInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=10, null=True, verbose_name='来源')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='标题')),
                ('url', models.CharField(blank=True, max_length=300, null=True, verbose_name='链接')),
                ('time', models.DateField(blank=True, null=True, verbose_name='日期')),
            ],
            options={
                'verbose_name': '敏感新闻',
                'verbose_name_plural': '敏感新闻',
            },
        ),
    ]
