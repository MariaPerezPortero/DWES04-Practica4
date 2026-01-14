from django.shortcuts import render
from .models import Perfil
from django.contrib.auth.models import User

# Create your views here.
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})

def listado_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/listado.html', {'usuarios': usuarios})
