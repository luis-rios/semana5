from django.urls import path

from materias.views import MateriaView

app_name = 'materias'

urlpatterns = [
    path('', MateriaView.as_view(), name='materia')
]
