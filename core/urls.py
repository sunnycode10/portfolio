from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('chat-api/', views.chat_api, name='chat_api'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]
