import datetime
from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(u"标题",max_length=255)
    brief = models.CharField(u"文章介绍",null=True,blank=True,max_length=255)
    category = models.ForeignKey('Category')
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile")
    pub_date = models.DateTimeField(blank=True,null=True)
    last_modify = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(u"优先级",default=1000)
    head_img = models.ImageField(u"标题图片",blank=True,null=True,upload_to="img")
    status_choices = (
        ('draft',u"草稿"),
        ('published',u"已发布"),
        ('hidden',u"隐藏")
    )
    status = models.CharField(choices=status_choices,default='published',max_length=64)
    def __str__(self):
        return self.title
    def clean(self):
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(("Draft entries may not have a publication date"))
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u"所属文章")
    parent_comment = models.ForeignKey('self',related_name='my_children',blank=True,null=True)
    comment_type_choices = (
        (1,u'评论'),
        (2,u"点赞")
                            )
    comment_type = models.IntegerField(choices=comment_type_choices,default=1)
    user = models.ForeignKey("UserProfile")
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.comment_type ==1 and len(self.comment) == 0:
            raise ValidationError(u"评论内容不能为空")


    def __str__(self):
        return "%s ,P: %s , %s" %(self.article,self.parent_comment,self.comment)

class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)
    brief = models.CharField(u"文章介绍",null=True,blank=True,max_length=255)
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField("UserProfile",blank=True)
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255,blank=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)

    def __str__(self):
        return self.name