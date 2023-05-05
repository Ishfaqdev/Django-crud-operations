from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=25)
    f_name = models.CharField(max_length=25)
    address = models.CharField(max_length=30)
    department = models.CharField(max_length=25)
    semester = models.IntegerField()
