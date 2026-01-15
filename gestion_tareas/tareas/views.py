from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm

#Si esta logueado se crea la tarea
@login_required
def tareas_alumno(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.creador = request.user  
            tarea.save()
            form.save_m2m()  
            return redirect('tareas_alumno')
    else:
        form = TareaForm()
        
    mis_tareas = Tarea.objects.filter(creador=request.user).distinct()
    
    return render(request, 'tareas/tareas_alumno.html', {
        'tareas': mis_tareas, 
        'form': form
    })
    
#Tareas pendiente de validación del profesor
def tareas_pendientes_validacion(request):
    tareas_pendientes = Tarea.objects.filter(validada_profe=False, requiere_validacion=True)
    return render(request, 'tareas/tareas_profesor.html', {'tareas': tareas_pendientes})


#Validación completada de la tarea
def validar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.validada_profe = True
    tarea.completada = True
    tarea.save() # Esto es lo que confirma la validación en Postgres
    return redirect('tareas_profesor')
