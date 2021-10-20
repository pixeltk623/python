from django.db import models

class Employee(models.Model):
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=gender)