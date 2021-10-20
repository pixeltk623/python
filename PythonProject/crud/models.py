from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=150,  null=True )
    file_upload = models.CharField(max_length=150,  null=True )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
