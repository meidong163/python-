from django.shortcuts import render
from .models import *
from django.db.models import *
from django.core.paginator import *
from django.http import HttpResponse, JsonResponse

# 渲染 首页
def index(request):
    listGoods = []
    i = 0
    while i < 6:
        listSrc = GoodsInfo.objects.filter(gtype_id=i+1).order_by('-gprice')[0:4]
        listDst = []
        for item in listSrc:
            listDst.append({'id':item.id,'gtitle':item.gtitle,'gprice':item.gprice,
                            'gpic':item.gpic})
        typename = item.gtype.title
        dicTemp = {'type':typename,'data':listDst}
        listGoods.append(dicTemp)
        i+=1
    content = {'listData':listGoods}
    # print(content)
    return render(request,'GoodsShow/index.html',content)
# 从页面上获取两个数据，分类id和页面id第几页
def list(request,typeId,pageId):
    #默认 页数是从url中传过来的
    if typeId=='':
        typeId = '1'
    if pageId=='':
        pageId = '1'
    #查分类的数据
    listSrc = GoodsInfo.objects.filter(gtype_id=int(typeId)).order_by('-gprice')

    #分页处理 每页放15条数据
    paginator = Paginator(listSrc,10)
    try:
        page_default = paginator.page(int(pageId))
    except PageNotAnInteger:
        # 如果传过来的不是整数默认取第一页的数据
        page_default = paginator.page(1)
    except EmptyPage:
        # 如果页码太大，默认取最大的页码
        page_default = paginator.page(paginator.num_pages)

    #推荐商品部分，暂时取ID最大的，具体的业务逻辑也是查两个数据，具体什么数据和业务相关
    listRec_R = GoodsInfo.objects.filter(gtype_id=int(typeId)).order_by('-id')[0:2]

    context = {'page':page_default,'Rec':listRec_R,'typeId':typeId}
    return render(request,'GoodsShow/morelist.html',context)

def detail(request,goodsId):
    # 处理详情页面
    #1. 根据商品的id号查商品
    goods = GoodsInfo.objects.get(pk=int(goodsId))
    #2. 详情也的两个推荐商品
    typeid = goods.gtype_id
    listRec_R = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[0:2]

    context = {'goods':goods,'Rec':listRec_R,'goodId':goodsId}
    return render(request,'GoodsShow/detail.html',context)

