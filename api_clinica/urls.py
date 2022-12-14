from django.contrib import admin
from django.urls import path
from api import views as apiViews
from web_clinica import views as webViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webViews.index),
    
    
    path("paciente/", apiViews.PacientesVista.as_view()),
    path("paciente/<int:pk>", apiViews.PacienteDetalle.as_view()),
]
