from django.db import models

# Create your models here.

#  creating company model

class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', "IT"), ('NON IT', 'NON IT'), ('Mobile Phones', 'Mobile Phones')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager', 'manager'),('Software Developer', 'sd'),('Project Leader', 'pl')))
    company= models.ForeignKey(Company, on_delete=models.CASCADE)