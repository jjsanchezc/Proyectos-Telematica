from django.db import models
from django.core.validators import RegexValidator
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.TextField(max_length=35,verbose_name='nombre')
    edad=models.IntegerField (verbose_name='edad')
    correo=models.EmailField(max_length=35,verbose_name='correo')
    ciudad=models.TextField(verbose_name='ciudad')
    direccion=models.TextField(verbose_name='direccion')
    
    def __str__(self):
        fila='Usuario con nombre: '+Usuario.nombre+'- edad: '+Usuario.edad+'- correo electronico: '+Usuario.correo+'- ciudad: '+Usuario.ciudad+'- direccion: '+Usuario.direccion
        return fila
