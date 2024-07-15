from rest_framework import serializers
from .models import Patient, Arzt


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ArztSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arzt
        fields = '__all__'
