from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    hsn=models.CharField(max_length=13)
    gst=models.IntegerField(max_length=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField(default=0)
    unit=models.CharField(max_length=10)
    pieces_in_packets=models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.name