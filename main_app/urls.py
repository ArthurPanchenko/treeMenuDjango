from django.urls import path
from . import views


urlpatterns = [
    path('category/<str:title>/', views.category, name='category'),
    path('', views.index, name='home'),
]