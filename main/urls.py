from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('book/', views.book, name= 'book'),
    path('about/', views.about, name= 'about'),
    path('menu/', views.menu, name= 'menu'),
    path('menu_item/<int:pk>/', views.display_menu_item, name= 'menu_item'),
]

