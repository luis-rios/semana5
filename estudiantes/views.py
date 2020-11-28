from django.shortcuts import render
from rest_framework import views, generics

from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializer


class EstudianteView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
