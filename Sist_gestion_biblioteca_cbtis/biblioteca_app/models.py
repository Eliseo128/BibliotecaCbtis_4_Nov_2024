from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    copias = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo