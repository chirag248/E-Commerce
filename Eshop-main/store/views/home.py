from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        buy = request.POST.get('buy')
        addtocart = request.POST.get('addtocart')
        quan = int(request.POST.get('quantity'))
        color = request.POST.get('color')
        size = request.POST.get('size')
        product_id = request.POST.get('product')
        cart = request.session.get('cart')
        product=f"{product_id}_{color}_{size}"
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = cart[product]+quan
            else:
                cart[product] = quan

                    # if quantity<=1:
                    #     cart.pop(product)
                    # else:
                    #     cart[product]  = quantity-1
        else:
            cart = {}
            cart[product] = quan
        request.session['cart'] = cart
        if buy:
            return redirect('cart')
        print('cart' , request.session['cart'])
        return redirect(f'product-detail/{product_id}')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


