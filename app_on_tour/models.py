from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    password = models.CharField(max_length=100)

class Curso(models.Model):
    colegio = models.CharField(max_length=100)
    nivel_curso = models.CharField(max_length=100)
    cantidad_alumnos = models.IntegerField()
    servicio = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_viaje = models.DateField()
    monto_depositado = models.IntegerField()
    meta_monto = models.IntegerField()
    id_cliente = models.ForeignKey(User,on_delete=models.CASCADE)


