from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    hsn=models.CharField(max_length=13)
    gst=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField(default=0)
    unit=models.CharField(max_length=10)
    each_piece_in_packets=models.IntegerField(default=0, null=True, blank=True)
    pieces_in_packets=models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.name
#this model represent the customertables
class addCustomer(models.Model):
    customerid=models.CharField(primary_key=True)
    customername=models.CharField(max_length=100,null=False,blank=False)
    gstno=models.CharField(max_length=20,blank=True,null=True)
    customeraddress=models.CharField(max_length=200)
    customerstate=models.CharField(max_length=100)
    customertype=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=10)
    def __str__(self):
        return self.customername
    
#this model for logging details for the product
class productloggin(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    hsn=models.CharField(max_length=13)
    gst=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField(default=0)
    unit=models.CharField(max_length=10)
    each_piece_in_packets=models.IntegerField(default=0, null=True, blank=True)
    pieces_in_packets=models.IntegerField(default=0, null=True, blank=True)
    status=models.CharField(max_length=100)
    date=models.DateTimeField()
    def __str__(self):
        return self.name