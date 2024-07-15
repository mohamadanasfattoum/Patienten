from rest_framework import generics
from .models import Patient, Arzt
from .serializers import PatientSerializer,ArztSerializer


class PatientApiList (generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientApiDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer



class ArztApiList (generics.ListCreateAPIView):
    queryset = Arzt.objects.all()
    serializer_class = ArztSerializer


class ArztApiDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Arzt.objects.all()
    serializer_class = ArztSerializer