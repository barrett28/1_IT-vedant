from django.db import models

# Create your models here.

class UserModel(models.Model):
    user_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
