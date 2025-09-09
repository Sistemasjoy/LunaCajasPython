from django.db import models

# Create your models here.

class Puerto(models.Model):
    nombre= models.CharField(max_length=4)
    created_at= models.DateTimeField(auto_now=True)

