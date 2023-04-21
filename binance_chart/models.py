from django.db import models
#from django.con

# Create your models here.
class StockDatabase(models.Model):
    date = models.DateTimeField()
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name