from django.db import models

# Create your models here.
class Texto(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.CharField(max_length=5000)

    def __str__(self):
        return self.nombre

class Integrante(models.Model):
    nombre = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='static/taubrix/imagenes', default='static/taubrix/imagenes/no-img.jpg')

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='static/taubrix/imagenes', default='static/taubrix/imagenes/no-img.jpg')

    def __str__(self):
       return self.nombre

    class Meta:
        verbose_name_plural = 'Imagenes'