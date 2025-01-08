from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home')
        path('land/<int:pk>/', views.land_detail, name='lamd_detail')
        ]
