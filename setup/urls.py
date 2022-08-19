"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from MediaApp.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Videos', VideoViewSet, basename='Video')
router.register('Categorias', CategoriaViewSet, basename='Categoria')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Videos/<int:pk>/', VideoEspecificoViewSet.as_view()),
    path('Categorias/<int:pk>/', CategoriaEspecificaViewSet.as_view()),
    path('Categorias/<int:id>/Videos/', VideosDaCategoriaViewSet.as_view())
]
