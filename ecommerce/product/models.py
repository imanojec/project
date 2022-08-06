from django.db import models

# Create your models here.

class Login(models.Model):
    UserId=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=500)
    Password=models.CharField(max_length=500)
