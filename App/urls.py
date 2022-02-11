from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('Auth.urls'), name='auth'),
    url('result/(?P<id>\d+)$', views.result, name='result')
]