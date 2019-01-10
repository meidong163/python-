from django.conf.urls import url
from . import views

urlpatterns = [
    # 默认情况去处理
    url(r'^register/$', views.register),
    url(r'^register_handle/$',views.register_handle),

    url(r'^login/$',views.login),
    url(r'^login_check/$',views.login_check),
    url(r'^usercenterinfo/$',views.user_center_info),
    url(r'^usercentersit/$',views.user_center_site),
    url(r'^getsession/$',views.getsession),
    url(r'^logout/$',views.logout),
]