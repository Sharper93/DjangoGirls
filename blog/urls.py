# blogs/
# blogs folder
    
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #url that thas post_list needs to execute a views function called post list
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # url that has post_detail needs to execute a views function called post
    path('post/new/', views.post_new, name='post_new'), # adding new path for post_new
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]