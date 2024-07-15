from django.db import models
from django.contrib.auth.models import User
class Patient(models.Model):
    KRANK = (
    ('Ja','Ja'),
    ('Nein','Nein'),
    )
    user = models.ForeignKey(User, related_name='patient_melder', on_delete=models.CASCADE, null=True, blank=True)
    patient = models.CharField(max_length=50)
    patient_situation = models.TextField(max_length=1000, null=True, blank=True)
    alt = models.IntegerField()
    krank = models.CharField(max_length=50, choices=KRANK , null=True, blank=True)
    medikamente = models.TextField(max_length=500)
    arzt = models.ForeignKey('Arzt', related_name='patient_arzt', on_delete=models.CASCADE, null=True, blank=True)



class Arzt(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    web_seite = models.CharField(max_length=50)
    tel = models.FloatField()


    

