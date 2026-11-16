from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=30)
    course=models.CharField(max_length=40)
    fee=models.DecimalField(max_digits=8,decimal_places=2)
    joining_date=models.DateField(max_length=30)
    is_fee_paid=models.BooleanField(default=False)
    
