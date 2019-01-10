from django.db import models

# 数据库的表 对象化，不用写sql
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey(BookInfo, on_delete=models.CASCADE,)
