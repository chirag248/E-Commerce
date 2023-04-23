from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    def get(self , request):
        if request.session.get('cart'):
            prod = list(request.session.get('cart').keys())
            ids = [int(product.split("_")[0]) for product in prod]
            products = Products.get_products_by_id(ids)
            for i in range(len(products)):
                products[i]['prod']=prod[i]
                products[i]['color']=prod[i].split("_")[1]
                products[i]['size']=prod[i].split("_")[2]
            print(products)
            return render(request , 'cart.html' , {'products' : products } )

def delete(request,id):
    cart=request.session.get('cart')
    if cart:
        quantity = cart.get(id)
        if quantity:
            cart.pop(id)
            request.session['cart']=cart
    return redirect('cart')
