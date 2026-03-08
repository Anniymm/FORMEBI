from django import forms
from .models import Product

# 1 - forms.Form -> Regular forms -> ar aris dakavshirebuli modelebtan - not db - magalitad vinmes sakontaqto ro ar gvinda shevinaxot bazashi
# 2 - forms.ModelForm -> Model_Based FOrm -> dakavshirebulia modeltan  -> db

class ProductForm(forms.ModelForm):
    class Meta: # es aucilebelia
        model = Product
        fields = ["name", "price", "in_stock"]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=100)
