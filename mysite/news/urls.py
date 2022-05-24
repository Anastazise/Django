from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #переход на главную страницу
    
]