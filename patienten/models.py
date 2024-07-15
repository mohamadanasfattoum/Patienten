from django.db import models
from django.contrib.auth.models import User
class Patient(models.Model):
    KRANK = (
    ('Ja','Ja'),
    ('Nein','Nein'),
    )
    user = models.ForeignKey(User, related_name='patient_melder', on_delete=models.CASCADE, null=True, blank=True)
    patient = models.CharField(max_length=50)
    alt = models.IntegerField()
    patient_ty = models.CharField(max_length=50, choices=KRANK)
    medikamente = models.TextField(max_length=500)
    arzt = models.ForeignKey('Arzt', related_name='patient_arzt', on_delete=models.CASCADE, null=True, blank=True)



class Arzt(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    web_seite = models.CharField(max_length=50)
    medikamente = models.TextField(max_length=500)
    tel = models.FloatField()
    

