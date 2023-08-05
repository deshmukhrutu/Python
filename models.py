from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

class Event(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.cascade)
    event_type=models.CharField(max_length=50)
    event_date=models.DateField()
class EmailTemplate(models.Model):
    event_type=models.CharField
    template=models.TextField()