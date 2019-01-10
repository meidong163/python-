from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^index/',views.index),
    url(r'list(\d*)/(\d*)$',views.list),
    url(r'^detail(\d+)',views.detail),
]