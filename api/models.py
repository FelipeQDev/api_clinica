from django.db import models
from rest_framework import serializer
# Create your models here.

#Paciente
class Paciente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad_paciente = models.IntegerField()
    
    class Meta:
        db_table = "paciente"

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"
#Doctor
class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=25)
    evaluacion_doc = models.IntegerField()
    horario_atencion = models.DateTimeField()
    disponible= models.BooleanField()
    
    class Meta:
        db_table = "doctor"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

#Horas
class HorasMedicas(models.Model):
    fecha_horaMed = models.DateTimeField()
    valor_hora = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor_encargado = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        db_table = "horas_medicos"

class HorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorasMedicas
        fields = "__all__"