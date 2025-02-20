# blogs\
    
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #url that thas post_list needs to execute a views function called post list
]