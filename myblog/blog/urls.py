# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('post_detial/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_edit<int:pk>', views.post_edit, name='post_edit'),
    path('post_delete<int:pk>/', views.post_delete, name='post_delete'),
     path('dashboard/', views.dashboard, name='dashboard'),

]
