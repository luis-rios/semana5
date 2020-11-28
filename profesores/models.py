from django.db import models

from estudiantes.models import Estudiante
from materias.models import Materia


class Profesor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    enrollment = models.IntegerField(default=True)
    schedule = models.DateTimeField()

    estudiantes = models.ManyToManyField(Estudiante, related_name='profesor')
    materias = models.ManyToManyField(Materia, related_name='profesor')

    def __str__(self):
        return self.name
