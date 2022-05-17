from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('<int:id>', views.detail,name='detail'),
    path('rooms', views.roomlist,name='rooms'),
    path('new', views.new,name='new'),

]