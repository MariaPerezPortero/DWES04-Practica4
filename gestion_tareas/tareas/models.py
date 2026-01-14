from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    TIPO_TAREA = (
        ('individual', 'Individual'),
        ('grupal', 'Grupal'),
        ('evaluable', 'Evaluable')
    )
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_TAREA)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_creadas')
    colaboradores = models.ManyToManyField(User, blank=True, related_name='tareas_colabora')
    requiere_validacion = models.BooleanField(default=False)
    completada = models.BooleanField(default=False)
    validada_profe = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo 
