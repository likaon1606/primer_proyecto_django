from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # on_delete=models.CASCADE es para eliminar archivos en cascada, es decir, si tiene relación con otra tabla, ambas se puedan eliminar
    