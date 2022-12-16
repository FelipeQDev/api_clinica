from django.contrib import admin
from django.urls import path
from api import views as apiViews
from web_clinica import views as webViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webViews.index),
    
    
    path("pacientes/", apiViews.PacientesVista.as_view(), name="verPacientes"),
    path("pacientes/ingresarPaciente", apiViews.PacientesVista.as_view(), name="ingresarPaciente"),
    path("pacientes/<int:pk>", apiViews.PacienteDetalle.as_view()),
    
    
    
    path("doctores/", apiViews.DoctoresVista.as_view()),
    path("doctores/<int:pk>", apiViews.DoctoresDetalle.as_view()),
    
    
    
    
    path("horas/", apiViews.Ficha_atencionVista.as_view()),
]
