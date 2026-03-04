from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# HTTP methods 
# POST - gagzavna = info rom sheviyvano
# GET - Migheba 
# PUT - cvlileba 
# DELETE - washla 

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list") # roca formas sheavsebs rom gadamamisamartos rame gverdze
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", { "form": form })


# csrf token ----> 

def product_list(request):
    products = Product.objects.all()
    # print(products) # queryset 
    # <QuerySet [<Product: Python-Spot<QuerySet [<Product: Python-Spotify>, <Product: NotificationService>]>
    return render(request, "products/product_list.html", {"products": products })
