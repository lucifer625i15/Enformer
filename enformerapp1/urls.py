from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog,name='blog'),
   path('home/', views.index,name="enformerapp1"),
   path('login/', views.loginUser,name="login"),
   path('logout/', views.logoutUser,name="logout"),
   path('register/', views.register,name='register'),
   path('profile/', views.profile,name='profile'),
   path('dashboard/', views.dashboard,name='dashboard'),
   path('post/<int:id>/', views.post ,name='post'),
   path('details/', views.details ,name='details'),
   path('edit/<int:id>/', views.edit ,name='edit'),
   path('add/', views.add ,name='add'),
   # path('main', views.main ,name='main'),
   path("delete-post/<int:id>/", views.delete_post, name="delete-post"),

   # path("about",views.about, name='about'),
   # path("services",views.services, name='services'),
]