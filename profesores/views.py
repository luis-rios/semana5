from django.shortcuts import render
from rest_framework import views, generics

from profesores.models import Profesor
from profesores.serializers import ProfesorSerializer


class ProfesorView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
