from django.urls import path
from . import views
from .views import chatbot_response

urlpatterns = [
        path('', views.home, name='home'),
        path('land/<int:pk>/', views.land_detail, name='lamd_detail'),
        path('accounts/register/', views.register, name='register'),
        path('api/chatbot/', chatbot_response, name='chatbot'),
        path('predict/', views.predict_price, name='predict_price'),
        ]
