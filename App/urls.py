from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('Auth.urls'), name='auth'),
    path('history/', views.history, name="history"),
    url('result/(?P<id>\d+)$', views.result, name='result'),
    url('questions/(?P<id>\d+)$', views.questions, name='questions'),
    url('test/(?P<id>\d+)$', views.test, name='test')
]