from django.shortcuts import render, redirect
from api.models import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def pacientes(request):
    paciente = Paciente.objects.all()
    return render(request, "pacientes.html", {"pacientes": paciente})


def ingresarPaciente(request):
    if request.method == 'POST':
        paciente = Paciente()
        paciente.nombre = request.POST["nomPaciente"]
        paciente.apellido = request.POST["apePaciente"]
        paciente.direccion = request.POST["dircPaciente"]
        paciente.ciudad = request.POST["ciudPaciente"]
        paciente.edad_paciente = request.POST["edadPaciente"]
        paciente.save()
        return redirect("verPacientes")
    return render(request, "pacientes.html", {"ingresar": "si"})


def doctores(request):
    doctor = Doctor.objects.all()
    data = {"doctor": doctor}
    return render(request, "doctores.html", data)
