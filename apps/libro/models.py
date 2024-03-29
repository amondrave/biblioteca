from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250,blank=False,null=False)
    apellido = models.CharField(max_length=250,blank=False,null=False)
    nacionalidad = models.CharField(max_length=100,blank=False,null=False)
    descripcion = models.TextField(blank=True,null=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nombre + self.apellido
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200,blank=False,null=False)
    fecha_publicacion = models.DateField('fecha de publicacion',blank=False,null=False)
    autor = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["nombre"]