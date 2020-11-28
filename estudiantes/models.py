from django.db import models


class Estudiante(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=True)
    sex = models.CharField(max_length=15)
    enrollment = models.IntegerField(default=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
