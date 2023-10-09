from django.db import models

# Create your models here.

class Curso(models.Model):
     curso = models.CharField(max_length=100)
     camada = models.IntegerField()