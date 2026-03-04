from django.urls import path
from .views import add_product,product_list

urlpatterns = [
    path("product_add/", add_product, name="add_product"),
    path("product/", product_list, name='product_list'),

]
