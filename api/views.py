from django.shortcuts import render
from rest_framework import mixins, generics

# Create your views here.

from api.models import*

# Definicion clase Pacientes con metodos GET Y POST
# Listar los todos los datos de Pacientes
class PacientesVista(mixins.ListModelMixin,  mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
    def get(self, request):
        return self.list(request)
    #Llamada a la BD los datos de la tabla Paciente
    def post(self, request):
        return self.create(request)
    
class PacienteDetalle(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
    #Obtener en la BD mediante por Primary Key, a un Paciente de la tabla
    def get(self, request, pk):
        return self.retrieve(request, pk)
    # Actualizar en la BD mediante por Primary Key, a un Paciente de la tabla
    def put(self, request, pk):
        return self.update(request, pk)
    # Borrar en la BD mediante la obtencion de la Primary Key, a un Paciente de la tabla
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    
# Doctores
class DoctoresVista(mixins.ListModelMixin,  mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def get(self, request):
        return self.list(request)
    #Llamada a la BD los datos de la tabla Doctores
    def post(self, request):
        return self.create(request)
    
class DoctoresDetalle(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    #Obtener en la BD mediante por Primary Key, a un Doctores de la tabla
    def get(self, request, pk):
        return self.retrieve(request, pk)
    # Actualizar en la BD mediante por Primary Key, a un Doctores de la tabla
    def put(self, request, pk):
        return self.update(request, pk)
    # Borrar en la BD mediante la obtencion de la Primary Key, a un Doctores de la tabla
    def delete(self, request, pk):
        return self.destroy(request, pk)
    

# ficha

class Ficha_atencionVista(mixins.ListModelMixin,  mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Ficha_Atencion.objects.all()
    serializer_class = Ficha_Serializer
    
    def get(self, request):
        return self.list(request)
    #Llamada a la BD los datos de la tabla Paciente
    def post(self, request):
        return self.create(request)
    
class Ficha_Detalle(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Ficha_Atencion.objects.all()
    serializer_class = Ficha_Serializer
    
    #Obtener en la BD mediante por Primary Key, a un Paciente de la tabla
    def get(self, request, pk):
        return self.retrieve(request, pk)
    # Actualizar en la BD mediante por Primary Key, a un Paciente de la tabla
    def put(self, request, pk):
        return self.update(request, pk)
    # Borrar en la BD mediante la obtencion de la Primary Key, a un Paciente de la tabla
    def delete(self, request, pk):
        return self.destroy(request, pk)