from django.contrib import admin
from .models import TypeInfo, GoodsInfo
# Register your models here.
# 使用admin 这个东西来维护 确保表已经完全生成

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = [
        'id', 'gtitle','gpic','gprice','gunit','gclick',
        'gkucun', 'gcontent',
    ]

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)