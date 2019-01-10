from django.db import models

# Create your models here.

# 用户中心的东西，但是实际开发的时候，要是一个全栈的工程师它要怎么开发呢？前端和后端要分开写么

# 用户表
class user(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    email = models.CharField(max_length=20,default='')
    address = models.CharField(max_length=40,default='')
    phone = models.CharField(max_length=11,default='')
    youbian = models.CharField(max_length=7,default='')
