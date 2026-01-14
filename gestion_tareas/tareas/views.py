from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm

@login_required # Obliga al alumno a estar logueado para ver la página
def tareas_alumno(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.creador = request.user
            tarea.save()
            return redirect('tareas_alumno')
    else:
        form = TareaForm()

    mis_tareas = Tarea.objects.filter(creador=request.user)
    return render(request, 'tareas/tareas_alumno.html', {'tareas': mis_tareas, 'form': form})

def tareas_pendientes_validacion(request):
    # Cambia .all() por .filter(validada_profe=False)
    tareas_pendientes = Tarea.objects.filter(validada_profe=False, requiere_validacion=True)
    return render(request, 'tareas/tareas_profesor.html', {'tareas': tareas_pendientes})
def completar_tarea(request, tarea_id):
    # Buscamos la tarea o devolvemos error 404 si no existe
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    # Solo se marca como completada si NO requiere validación del profe
    if not tarea.requiere_validacion:
        tarea.completada = True
        tarea.save()
    
    return redirect('tareas_alumno')

def validar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.validada_profe = True
    tarea.completada = True
    tarea.save() # Esto es lo que confirma la validación en Postgres
    return redirect('tareas_profesor')
