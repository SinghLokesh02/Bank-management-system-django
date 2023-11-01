from django.contrib import admin
from django.urls import path,include
from panel import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('show/',views.show,name='show'),
    path('search/',views.search,name='search'),
    path('transfer/',views.transfer,name='transfer'),
]
