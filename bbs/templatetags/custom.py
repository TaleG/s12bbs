#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter
def truncate_url(img_obj):
    if img_obj == None:
        pass
    else:
        return img_obj.name.split("/",maxsplit=1)[-1]#取掉setting中设置img路径，从而返回前端找到图片

@register.simple_tag
def filter_comment(article_obj):
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),#统计评论数
        'thumb_count':query_set.filter(comment_type=2).count(),#统计点赞数
    }
    return comments