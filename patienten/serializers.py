from rest_framework import serializers
from .models import Patient, Arzt, User


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    arzt = serializers.StringRelatedField()
    class Meta:
        model = Patient
        fields = '__all__'


class ArztSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arzt
        fields = '__all__'
