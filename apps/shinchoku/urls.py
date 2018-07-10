from django.urls import path

from . import views

app_name = 'shinchoku'

urlpatterns = [
    path('', views.index, name='index'),
    path('shinchoku/new', views.new, name='new'),
    ]
