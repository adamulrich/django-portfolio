from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('city_list.html', views.list),
    path('index.html', views.index),
]
