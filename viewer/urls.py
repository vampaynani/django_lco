from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='courses'),
  path('<str:slug>/', views.detail, name='detail')
]