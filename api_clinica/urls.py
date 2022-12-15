from django.contrib import admin
from django.urls import path
from api import views as apiViews
from web_clinica import views as webViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webViews.index, name="index"),
    
    
    path("paciente/", apiViews.PacientesVista.as_view(), name="pacientes"),
    path("paciente/<int:pk>", apiViews.PacienteDetalle.as_view()),
    
    
    
    path("doctores/", apiViews.DoctoresVista.as_view(), name="doctores"),
    
    path("horas/", apiViews.Ficha_atencionVista.as_view(), name="horas"),
]
