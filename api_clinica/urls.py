from django.contrib import admin
from django.urls import path
from api import views as apiViews
from web_clinica import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index, name="index"),
    
    #tablas
    path("pacientes/", v.pacientes, name="pacientes"),
    path("doctores/", v.doctores, name="doctores"),
    path("horas/", v.horas, name="horas"),
    
    
    #mixins
    path("api/paciente/", apiViews.PacientesVista.as_view(), name="pacienteMixins"),
    path("api/paciente/<int:pk>", apiViews.PacienteDetalle.as_view(), name="pacientePKmixins"),
    
    path("api/doctor/", apiViews.DoctoresVista.as_view(), name="doctorMixins"),
    path("api/doctor/<int:pk>", apiViews.DoctoresDetalle.as_view(), name="doctorPKmixins"),
    
    path("api/hora/", apiViews.Ficha_atencionVista.as_view(), name="horaMixins"),
    path("api/hora/<int:pk>", apiViews.Ficha_Detalle.as_view(), name="horaPKMixins"),
]
