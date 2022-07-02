import imp
from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.TodoList.as_view(), name="list"),
]
