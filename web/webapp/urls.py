"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='auth_login'),
    path('home/',views.home, name='home'),
    path('pharmacy/',views.pharmacy, name='pharmacy'),
    path('smartcard/',views.smartcard, name='smartcard'),
    path('chat', views.index, name='index'),
    path('chat-send', views.chat_api, name='chat_api'),
    path('register/', views.register, name='register'),
]
