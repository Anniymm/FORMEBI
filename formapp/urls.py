from django.urls import path
from .views import add_product,product_list, contact_view, update_product, delete_product

urlpatterns = [
    path("product_add/", add_product, name="add_product"),
    path("product/", product_list, name='product_list'),
    path("contact/", contact_view, name="contact_view"),
    path('update/<int:pk>', update_product, name="update_product"),
    path("delete/<int:pk>", delete_product, name="delete_product")
]
