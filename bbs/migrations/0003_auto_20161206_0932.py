# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_article_head_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='标题图片'),
        ),
    ]
