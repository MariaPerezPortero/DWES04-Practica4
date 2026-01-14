from django.urls import path
from . import views

urlpatterns = [
    # Verifica que diga views.tareas_alumno
    path('alumno/', views.tareas_alumno, name='tareas_alumno'),
    path('profe/', views.tareas_pendientes_validacion, name='tareas_profesor'),
    path('completar/<int:tarea_id>/', views.completar_tarea, name='completar_tarea'),
    path('validar/<int:tarea_id>/', views.validar_tarea, name='validar_tarea'),
]