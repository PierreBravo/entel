from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)