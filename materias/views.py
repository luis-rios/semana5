from django.shortcuts import render
from rest_framework import views, generics

from materias.models import Materia
from materias.serializers import MateriaSerializer


class MateriaView(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
