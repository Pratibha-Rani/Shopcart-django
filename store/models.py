from tkinter import CASCADE
from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) #models.CASCADE--> whenever a category is deleted items related to that category is also deleted 
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug]) 
# product_detail is the name of the path taken from urls.py for single product,Self---> means product ,category--> category defined inside product
# category.slug--> interconnected to category slug
    def __str__(self):
        return self.product_name
class VariationManager(models.Manager): # variation managers will allow you to modify the queryset
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color', is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size' ,is_active=True)



variation_category_choice=(
    ('color','color'),
    ('size','size'),
)
class Variation(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE) # for a particular variation  the product will be particular
    variation_category=models.CharField(max_length=100,choices=variation_category_choice)
    variation_value=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)
    objects=VariationManager()

    def __str__(self):
        return self.variation_value