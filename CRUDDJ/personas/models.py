from django.db import models

# Create your models here.
class Ciudad(models.Model):
    idCiudad=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    
class Persona(models.Model):
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    documento=models.BigIntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    correo=models.EmailField(max_length=50)
    clave=models.CharField(max_length=50)

