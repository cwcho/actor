from django.db import models

class Customer(models,Model):
    pwd         = models.CharField(max_langth=100)
    name        = models.CharField(max_langth=60)
    email       = models.EmailField(max_langth=75,unique)
    phone       = models.CharField(max_langth=30)
    address     = models.CharField(max_langth=500)

class Shop(models,Model):
    name        = models.CharField(max_langth=50)
    phone       = models.CharField(max_langth=30)
    address     = models.CharField(max_langth=500)

class Menu(models,Model):
    name        = models.CharField(max_langth=100)
    price       = models.PositiveIntegerField()

class Order(models,Model):
    customer    = models.ForeignKey(Customer)
    shop        = models.ForeignKey(Shop)
    bill        = models.PositiveIntegerField()
    date        = models.DateField()

class Order_specific(models,Model):
    order       = models.ForeignKey(Order)
    menu        = models.ForeignKey(Menu)
    qty         = models.PositiveSmallIntegerField()


# Create your models here.
