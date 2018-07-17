from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    github = models.URLField()
    description = models.CharField(max_length=1000)
