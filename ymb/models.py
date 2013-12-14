from django.db import models

class customer(models,Model):
    pwd     = models.CharField(max_langth=100)
    name    = models.CharField(max_langth=60)
    email   = models.EmailField(max_langth=75,unique)
    phone   = models.CharField(max_langth=30)
    address = models.CharField(max_langth=500)

class shop(models,Model):
    name    = models.CharField(max_langth=50)
    phone   = models.CharField(max_langth=30)
    address = models.CharField(max_langth=500)

class menu(models,Model):
    name    = models.CharField(max_langth=100)
    price   = models.PositiveIntegerField()

class order(models,Model):
    bill    = models.PositiveIntegerField()
    date    = models.DateField()

class order_specific(models,Model):
    pwd     = models.CharField(max_langth=100)


# Create your models here.
