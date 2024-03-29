"""resumepage_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    path('', views.index, name="index"),
    path('projects', views.index, name="index"),
    path('renders', views.index, name="renders"),
    path('about', views.index, name="about"),
    path('contact_me', views.index, name="contact_me"),
    path('project/<int:pk>', views.index, name="specific_project"),
    path('image/<int:pk>', views.index, name="specific_image"),
]
