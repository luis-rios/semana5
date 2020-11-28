from django.urls import path

from profesores.views import ProfesorView

app_name = 'profesores'


urlpatterns = [
    path('', ProfesorView.as_view(), name='profesor')
]
