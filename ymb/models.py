from django.db import models

from django.db import models

class Customer(models.Model):
    pwd         = models.CharField(max_length=100)
    name        = models.CharField(max_length=60)
    email       = models.EmailField(max_length=75, unique=True)
    phone       = models.CharField(max_length=30)
    address     = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class Shop(models.Model):
    name        = models.CharField(max_length=50)
    phone       = models.CharField(max_length=30)
    address     = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class Menu(models.Model):
    name        = models.CharField(max_length=100)
    price       = models.PositiveIntegerField()
    def __unicode__(self):
        return self.name

class Order(models.Model):
    customer    = models.ForeignKey(Customer)
    shop        = models.ForeignKey(Shop)
    bill        = models.PositiveIntegerField()
    date        = models.DateField()
    def __unicode__(self):
        return self.id

class Order_specific(models.Model):
    order       = models.ForeignKey(Order)
    menu        = models.ForeignKey(Menu)
    qty         = models.PositiveSmallIntegerField()
    def __unicode__(self):
        return self.id

