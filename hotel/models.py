from django.db import models

# Create your models here.

class Room(models.Model):
  image = models.ImageField(upload_to="images/")
  room_number = models.IntegerField(unique=True)
  type = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  amenities = models.TextField(blank=True)

class Guest(models.Model):
  name = models.CharField(max_length=100)
  contact_details = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
 


