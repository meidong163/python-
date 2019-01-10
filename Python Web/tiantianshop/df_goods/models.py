from django.db import models
from tinymce.models import HTMLField
# 首页的分类 图片为维护。
class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    # 图片类型
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    # 富文本编辑器 让商户更方便的设计简介部分的内容
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    # 维护一个分类



