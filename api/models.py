from django.db import models
from rest_framework import serializers
# Create your models here.

#Paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=20)
    edad_paciente = models.IntegerField()
    
    class Meta:
        db_table = "paciente"

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"
        
#Doctor
class Doctor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=25)
    url_imagen = models.CharField(max_length=1000)
    evaluacion_doc = models.IntegerField()
    horario_atencion = models.DateTimeField()
    disponibilidad= models.BooleanField()
    
    class Meta:
        db_table = "doctor"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        
#Ficha

class Ficha_Paciente(models.Model):
    motivo = models.CharField(max_length=40)
    prevision = models.CharField(max_length=15)
    horario = models.TimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "ficha_paciente"
        
class Ficha_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha_Paciente
        fields = "__all__"
        
        
#Detalle Horas
class Detalle(models.Model):
    fecha = models.DateTimeField()
    precio_total = models.IntegerField()

    class Meta:
        db_table = "detalle"

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = "__all__"