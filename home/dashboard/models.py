from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.

class ContactUs(models.Model):
    first_name= CharField(max_length=150)
    last_name= CharField(max_length=150)
    email= CharField(max_length=150)
    phone= CharField(max_length=150)
    address= CharField(max_length=150)
    created_date = DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name