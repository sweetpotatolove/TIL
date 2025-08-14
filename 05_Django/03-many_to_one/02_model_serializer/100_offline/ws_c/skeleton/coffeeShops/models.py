from django.db import models


# Create your models here.
class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name
