from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    # class Meta: # es archevitia, sheidzleba arc gauketot
    #     verbose_name = 'Product'
    #     verbose_name_plural = 'Product'

# form -> logic -> bazashi
# - user input 
# - validaciebi 
# - save db

# 1 - forms.Form -> Regular forms -> ar aris dakavshirebuli modelebtan - not db
# 2 - forms.ModelForm -> Model_Based FOrm -> dakavshirebulia modeltan  -> db

