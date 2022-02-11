from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.sign_out, name='logout'),
]
