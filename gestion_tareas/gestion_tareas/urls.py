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
from django.urls import path
from . import views

urlpatterns = [
    # Verifica que diga views.tareas_alumno
    path('alumno/', views.tareas_alumno, name='tareas_alumno'),
    path('profe/', views.tareas_pendientes_validacion, name='tareas_profesor'),
    path('completar/<int:tarea_id>/', views.completar_tarea, name='completar_tarea'),
    path('validar/<int:tarea_id>/', views.validar_tarea, name='validar_tarea'),
]