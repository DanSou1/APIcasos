from django.db import models

# Create your models here.
class Project(models.Model):
    area = models.CharField(max_length=200)
    description = models.TextField()
    ubication = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)  