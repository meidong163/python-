from django.db import models

#第二课，模型的应用

# 自定义管理器 不过自定义的管理器是在生成表之后写的，那如果写在表之前会有问题么？会报错
class BookInfoManager(models.Manager):
    # 1. 重写查询
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    # 2.自定义模型的构造函数。
# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    # 可以通过元类来自定义 管理器
    class Meta():
        db_table = 'bookinfo'
        bookManager1 = models.Manager()
        bookManager2 = BookInfoManager()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    # 完成一对多的映射关系
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


# 管理器的作用 完成表和模型类的映射
# 改变表结构（添加字段）修改字段的类型 需要重新迁移，重新迁移可删除迁移文件
