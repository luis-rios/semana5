from django.urls import path

from estudiantes.views import EstudianteView

app_name = 'estudiantes'


urlpatterns = [
   path('', EstudianteView.as_view(), name='estudiante')
]
