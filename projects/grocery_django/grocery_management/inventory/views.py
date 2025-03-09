from django.shortcuts import render, redirect
from .models import Products

# Create your views here.


def index(request):
    pd = Products.objects.all()
    return render(request, 'inventory/index.html', {'pd':pd})



def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        quantity = float(request.POST["quantity"])
        price = float(request.POST["price"])
        Products.objects.create(name=name, quantity=quantity, price=price)
        return redirect("home")
    return render(request, "inventory/add_product.html")




def update_stock(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == "POST":
        sold_quantity = float(request.POST["sold_quantity"])
        if sold_quantity <= product.quantity:
            product.quantity -= sold_quantity
            product.save()
        return redirect("home")
    return render(request, "inventory/update_stock.html", {"product": product})
