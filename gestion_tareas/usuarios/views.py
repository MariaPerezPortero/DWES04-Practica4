
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


#Perfil
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})


#Listado
def listado_usuarios(request):
    if request.method == 'POST':
        nombre = request.POST.get('username')
        clave = request.POST.get('password')
        es_profe = request.POST.get('es_profesor') == 'on'

        if nombre and clave:
            # Crear user en base de datos
            nuevo_usuario = User.objects.create_user(username=nombre, password=clave)
            
            if es_profe:
                nuevo_usuario.is_staff = True
                nuevo_usuario.save()
            
            messages.success(request, f"Usuario {nombre} creado con éxito.")
            return redirect('listado_usuarios')

    # Mostrar datos en tabla
    usuarios = User.objects.all()
    return render(request, 'usuarios/listado.html', {'usuarios': usuarios})