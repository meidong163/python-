from django.shortcuts import render,redirect
import hashlib
from .models import *
from django.http import *
import re
from .isLogin import *
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register/')

    # 密码加密
    # s1 = sha1()
    # s1.update(upwd)
    # upwd3 = s1.hexdigest()
    # upwd3 = hashlib.sha1((bytes(upwd,'utf-8'))).hexdigest() 以上写法会有问题

    hash_re = hashlib.md5()
    hash_re.update(upwd.encode('utf-8'))
    upwd3 = hash_re.hexdigest()
    print(hash_re.hexdigest())
    us = user() # 类名最好大写，如然会有问题。
    us.user = uname
    us.pwd = upwd3
    us.email = uemail
    us.save()
    print('success')
    #注册成功
    return redirect('/user/login/') #转的地址

def login(request):
    return render(request, 'df_user/login.html')
# @is_login
def login_check(request):
    # 获取用户数据
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    # 如果记住存在的话
    jizhu = request.POST.get('jizhu',0)
    # 是否记住登录的的用户的逻辑，下次访问如果有cookie传过来，就无需在输入密码登录了，可直接登录
    # refer = request.POST.get('refer')

    hash_re = hashlib.md5()
    hash_re.update(pwd.encode('utf-8'))
    upwd3 = hash_re.hexdigest()

    user_list = user.objects.filter(user=username)
    print(user_list[0].pwd,upwd3[0:20])
    # 由于数据库中字段设计20 因而只能比较20位
    if user_list[0].pwd == upwd3[0:20]:
        # 这一段还是有问题的，理解不了，可惜
        # url = request.COOKIES.get('url','/')
        # red = HttpResponseRedirect(url)
        # red.set_cookie(url,'',max_age=-1)
        #
        # # 判断是否记住密码，如果有记住密码的话这里需要设置下cookie
        # if jizhu != '':
        #     red.set_cookie('uname',user_list[0])
        # else:
        #     red.set_cookie('uname','')

        # 为用户创建session
        request.session['uname'] = username
        # 创建一个user_id的session，防止重新跳回
        request.session['user_id'] = user_list[0].id
        request.session.set_expiry(0)
        # 登录成功之后，需要在nav_bar 中显示已登录用户的相关信息。
        # print(red)
        # return red
        # red 包含了这种情况 从哪里来去显然哩个地址
        return redirect('/user/usercenterinfo/')
    else:
        #错误情况
        context = {'login':'error'}
        print('error')
        # return render(request,'df_user/login.html',context)
        return render(request,'df_user/login.html',context)
    # 如果正常登录就去显示 货物
    # 如果没有，就没办法显示

def user_center_info(request):
    # 登录之后进入用户中心 session并没有给数据库中存
    name = request.session.get('uname')
    print(name)
    if name!=None:
        a = user.objects.filter(user=name)
        if a.exists()==True:
            context = {'statu': 'login', 'user': a[0], 'pageName': '用户中心'}
            return render(request, 'df_user/user_center_info.html', context)
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    return render(request,'df_user/user_center_info.html')

def user_center_site(request):
    return render(request,'df_user/user_center_site.html')

def getsession(request):
    print(request)
    uname = request.session.get('uname')
    return JsonResponse({'uname': uname})

def logout(request):
    request.session.flush()
    return redirect('/')