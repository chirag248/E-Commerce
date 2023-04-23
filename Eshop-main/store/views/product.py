from django.shortcuts import render 
from store.models.product import Products, Product_attribute
from django.views import View

class Product(View):
    def get(self, request, id):
        product_details = Products.get_products_by_ids(id)
        product_details.specifications = product_details.specifications.split(",") if product_details.specifications else None
        product_attr = Product_attribute.objects.filter(product_id=id)
        product_attr_dict = {}
        product_attr_dict["size"] = set([size.sizes.size_num for size in product_attr])
        product_attr_dict["color"] = set([size.colors.color_name for size in product_attr])
        data = {}
        data['products'] = product_details
        data['product_attr'] = product_attr_dict
        data['quantity'] = 1
        
        return render (request, 'products.html', data)
    def post(self,request,id):
        size1=request.POST.get("size")
        color1=request.POST.get("color")
        plus = request.POST.get('plus')
        minus = request.POST.get('minus')
        quantity = int(request.POST.get('quantity'))
        product_details = Products.get_products_by_ids(id)
        product_details.specifications = product_details.specifications.split(",") if product_details.specifications else None
        product_attr = Product_attribute.objects.filter(product_id=id)
        product_attr_dict = {}
        product_attr_dict["size"] = set([size.sizes.size_num for size in product_attr])
        product_attr_dict["color"] = set([size.colors.color_name for size in product_attr])
        data = {}
        data['products'] = product_details
        data['product_attr'] = product_attr_dict
        data['quantity'] = quantity
        if plus:
            data['quantity'] = data['quantity']+1
        if minus and quantity>1:
            data['quantity'] = data['quantity']-1
        data['size1'] = size1
        data['color1'] = color1
        print("hi",data['quantity'])
        return render (request, 'products.html', data)


