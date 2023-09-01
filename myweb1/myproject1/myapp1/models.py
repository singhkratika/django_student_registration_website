from django.db import models

# Create your models here.
class Student(models.Model):
    sturollno=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=60)
    branch=models.CharField(max_length=60)
    email=models.CharField(max_length=60)