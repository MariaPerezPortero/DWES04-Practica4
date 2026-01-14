from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.listado_usuarios, name='listado_usuarios'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario')
]
