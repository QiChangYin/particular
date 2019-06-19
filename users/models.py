# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class BaseTable(models.Model):
    """
    公共字段列
    """
    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)


class UserInfo(BaseTable):
    """
    用户注册信息表
    """
    class Meta:
        verbose_name = "用户信息"
        db_table = "UserInfo"

    username = models.CharField(verbose_name='用户名', max_length=20, unique=True, null=False)
    password = models.CharField(verbose_name='登陆密码', max_length=100, null=False)
    email = models.EmailField(verbose_name='用户邮箱', unique=True, null=False)


class UserToken(BaseTable):
    """
    用户登陆token
    """
    class Meta:
        verbose_name = "用户登陆token"
        db_table = "UserToken"

    user = models.OneToOneField(UserInfo, verbose_name="用户", on_delete=models.CASCADE)
    token = models.CharField(verbose_name='token', max_length=50, blank=True,null=True)
