"""
URL configuration for StudentHelp project.

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
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin, auth

urlpatterns = [
    path('admin/',admin.site.urls),
    path('poste/', include('poste.urls')),
    path('reaction/',include('reaction.urls')),
    path('user/', include('user.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signIn/',auth_views.LoginView.as_view(template_name='signIn.html'), name = 'signIn'),
    path('signOut/',auth_views.LogoutView.as_view(template_name='logout.html'), name ='signOut'),
    path('signUp/',views.register, name='signUp'),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", views.index),
]
