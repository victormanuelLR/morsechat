from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='room'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('<slug:slug>/', views.room, name='room'),
]