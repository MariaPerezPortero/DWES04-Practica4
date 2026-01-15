from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from usuarios.views import listado_usuarios 

urlpatterns = [
    path('admin/', admin.site.urls),
    #Login
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    #Listado
    path('usuarios/lista/', listado_usuarios, name='listado_usuarios'),
    #Usuarios
    path('usuarios/', include('usuarios.urls')),
    #Tareas
    path('tareas/', include('tareas.urls')),
]