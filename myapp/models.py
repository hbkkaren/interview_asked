from django.db import models

# Create your models here.


class Admin(models.Model):

    fullName = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.fullName
    
class Product(models.Model):
    productCompany = models.CharField(max_length=100)


class Orderplace(models.Model):
    address = models.CharField(max_length=50,default="")
    admin = models.ForeignKey(Admin,on_delete= models.CASCADE)
    product = models.ForeignKey(Product,on_delete= models.CASCADE)

