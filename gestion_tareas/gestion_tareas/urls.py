"""
URL configuration for gestion_tareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from usuarios.views import listado_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    #Listado
    path('usuarios/lista/', listado_usuarios, name='listado_usuarios'),
    #Login
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    #Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    #Usuarios
    path('usuarios/', include('usuarios.urls')),
    #Tareas
    path('tareas/', include('tareas.urls')),
]