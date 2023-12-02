from django.shortcuts import render
from .models import Admin,Product,Orderplace

# Create your views here.


def index(request):
    if request.method =="POST":
        
    
        admin=Admin.objects.create(
            fullName = request.POST['fullName'],
            mobile = request.POST['mobile'],
            email = request.POST['email'],
        )
        product=Product.objects.create(
            productCompany = request.POST['productCompany']
        )
        Orderplace.objects.create(
            address = request.POST['address'],
            admin=admin,
            product=product
        )
        return render(request,"Order.html")
        
    return render(request,"index.html")


def clear(request):
    return render (request,"index.html")