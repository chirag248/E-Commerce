from django.db import models
from .category import Category
class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')
    size= models.BooleanField(default= False)
    specifications= models.CharField(max_length=250, help_text="seperate it by ,", null=True)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids).values()

    @staticmethod
    def get_products_by_ids(id):
        return Products.objects.get(id=id)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()

class Size(models.Model):
    size_num = models.CharField(max_length=10, help_text="XS,S,M,L,XL,XXL so on")

class Color(models.Model):
    color_name = models.CharField(max_length=15, help_text="RED")


class Product_attribute(models.Model):
    product = models.ForeignKey('Products', related_name="product_attrs", on_delete=models.CASCADE)
    sizes = models.ForeignKey('Size', related_name="product_sizes", on_delete=models.CASCADE, null=True)
    colors = models.ForeignKey('Color', related_name="product_colors", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) 