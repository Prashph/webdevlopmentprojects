from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name= models.CharField(max_length=122)
    last_name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    decs= models.TextField()
    