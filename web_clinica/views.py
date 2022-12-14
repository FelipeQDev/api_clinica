from django.shortcuts import render
from api.models import Paciente
# Create your views here.

def index(request):
    return render(request, "index.html")

def pacientes(request):
    paciente = Paciente.objects.all()
    data = {"listarPacientes" : paciente}
    return render(request, "pacientes.html", data)
