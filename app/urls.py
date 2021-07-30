from . import views
from django.urls import path
#from rest_framework import routers

urlpatterns = [
    path('getposts', views.getPosts, name='post_list'),
    path('', views.postList, name='posts'),
    #path('create', views.postCreate.as_view(), name='create'),
    path('create', views.postCreate, name='create'),
    path('detail/<str:pk>', views.postDetail, name='detail'),
    path('update/<str:pk>', views.postUpdate, name='update'),
    path('delete/<str:pk>', views.postDelete, name='delete'),
 ]



