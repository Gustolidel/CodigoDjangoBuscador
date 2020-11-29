"""Evaluación2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from e2app.views import DepartamentoAPIView,DistritoAPIView,ProvinciaAPIView,\
    InstitucionAPIView,TipoInstitucionAPIView,InstitucionRUCAPIView,InstitucionTipoAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Departamentos/', DepartamentoAPIView.as_view()),
    path('Distrito/',DistritoAPIView.as_view()),
    path('Provincia/',ProvinciaAPIView.as_view()),
    path('Institucion/',InstitucionAPIView.as_view()),
    path('TipoInstitucion/',TipoInstitucionAPIView.as_view()),
    path('RUCInstitucion/',InstitucionRUCAPIView.as_view()),
    path('InstitucionTipoApi/',InstitucionTipoAPIView.as_view()),
]
