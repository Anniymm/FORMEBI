from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, ContactForm
from .models import Product
from django.core.paginator import Paginator

# HTTP methods 
# POST - gagzavna = info rom sheviyvano
# GET - Migheba 
# PUT - cvlileba 
# DELETE - washla 

# ---------------------
# POST
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

# -----------------------------------------
# GET - paginations - gverdebi 
def product_list(request):
    products = Product.objects.all()

    paginator = Paginator(products, 5) # 5 erteuli ert gverdze 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "products/product_list.html", {"page_obj": page_obj })

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data["message"]
            return redirect("product_list")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
        

# ---------------------------
# PUT - Update
# konkretul products -> mogvaqvs info -> infos vcvlit da vagzavnit 
# ..../product/1
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product) #instance arsebuli productia 
        if form.is_valid():
            form.save()
    else:
        form = ProductForm(instance=product)
    return render(request, "products/add_product.html", {"form": form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    
    return render (request, "products/delete_product.html", {"product": product})
