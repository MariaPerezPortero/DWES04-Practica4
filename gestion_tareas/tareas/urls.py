from django.urls import path
from . import views

urlpatterns = [

    path('alumno/', views.tareas_alumno, name='tareas_alumno'),
    path('profe/', views.tareas_pendientes_validacion, name='tareas_profesor'),
    path('validar/<int:tarea_id>/', views.validar_tarea, name='validar_tarea'),
]