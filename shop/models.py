from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
    
class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=256)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    total=models.FloatField(default=0.0)
    def __str__(self) -> str:
        return self.name

    
