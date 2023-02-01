from django.db import models

# Create your models here.
class details(models.Model):
    Name=models.CharField(max_length=120)
    Email=models.EmailField(max_length=100)
    Phone=models.IntegerField()
    Country=models.CharField(max_length=100)
    City=models.CharField(max_length=120)
    Query=models.TextField()