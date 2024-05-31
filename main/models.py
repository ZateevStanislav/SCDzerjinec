from django.db import models

class Student(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthdate = models.DateField()