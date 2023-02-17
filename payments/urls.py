from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("item/<int:pk>", views.ItemPageView.as_view(), name="item"),
]
