from django.urls import path
from . import views

urlpatterns = [
    path('init', views.InitializeAccountApiView.as_view(), name='initialize'),
]

