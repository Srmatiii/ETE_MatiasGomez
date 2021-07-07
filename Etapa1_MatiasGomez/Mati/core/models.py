from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Colaboradores(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='rut')
    image = models.ImageField(upload_to='images/', null=True, blank = True)     
    nombreComp = models.CharField(max_length=40, verbose_name='Nombre completo')     
    telefono = models.CharField(max_length=9, verbose_name='Numero de telefono')     
    direccion =  models.CharField(max_length=30, verbose_name='Direccion')     
    email = models.CharField(max_length=30, verbose_name='Email')     
    contrasenia = models.CharField(max_length=30, verbose_name='Contraseña')     
    pais = models.CharField(max_length=15, verbose_name='Pais')     
    
    def str(self):         
        return(self.nombreComp)