from django.db import models
from rest_framework import serializers
# Create your models here.

# Paciente


class Paciente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=20)
    edad_paciente = models.IntegerField()

    class Meta:
        db_table = "paciente"

    def __str__(self):
        return str(self.nombre + " " + self.apellido)


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

# Doctor


class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=25)
    url_imagen = models.CharField(max_length=1000)
    horario_atencion = models.TimeField()
    evaluacion_doc = models.DecimalField(decimal_places=1, max_digits=2)
    disponibilidad = models.BooleanField()

    class Meta:
        db_table = "doctor"
        

    def __str__(self):
        return str(self.nombre + " " + self.apellido+" " + "("+self.especialidad+")")


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"


# Ficha de atencion de paciente
class Ficha_Atencion(models.Model):
    motivo = models.CharField(max_length=40)
    prevision = models.CharField(max_length=15)
    fecha = models.DateTimeField()
    precio_total = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        db_table = "ficha_atencion"


class Ficha_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha_Atencion
        fields = "__all__"
