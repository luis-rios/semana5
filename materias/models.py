from django.db import models

from estudiantes.models import Estudiante


class Materia(models.Model):
    name = models.CharField(max_length=50)
    schedule = models.DateTimeField()

    estudiantes = models.ManyToManyField(Estudiante, related_name='materia')

    def __str__(self):
        return self.name
