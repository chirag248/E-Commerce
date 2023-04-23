from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from store.models.product import Products, Product_attribute, Size, Color
from Eshop.paytm import Checksum
from store.models.orders import Order
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'jd#3&lCd_f43eBpd'

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        total = request.POST.get('total')
        ids = {int(i.split("_")[0]):[i.split("_")[1],i.split("_")[2],i] for i in list(cart.keys())}
        products = Products.get_products_by_id(ids.keys())
        
        for product in products:
            order = Order(customer=Customer(id=customer),
                          product_id=product.get('id'),
                          size=Size.objects.get(size_num=ids.get(product.get('id'))[1]),
                          color=Color.objects.get(color_name=ids.get(product.get('id'))[0]),
                          price=product.get('price'),
                          address=address,
                          phone=phone,
                          quantity=cart.get(ids.get(product.get('id'))[2]))
            quantit=Product_attribute.objects.filter(product_id=product.get('id'),colors__color_name=ids.get(product.get('id'))[0],sizes__size_num=ids.get(product.get('id'))[1])
            if quantit[0].quantity >= cart.get(ids.get(product.get('id'))[2]):
                 order.save()
                 quantit.update(quantity =quantit[0].quantity-int(cart.get(ids.get(product.get('id'))[2])))
                 request.session['cart'] = {}
                 param_dict={

                 'MID': 'JcNIyz35089929051435',
                 'ORDER_ID': str(order.id),
                 'TXN_AMOUNT': str(total),
                 'CUST_ID': Customer.objects.get(id=customer).email,
                 'INDUSTRY_TYPE_ID': 'Retail',
                 'WEBSITE': 'WEBSTAGING',
                 'CHANNEL_ID': 'WEB',
                 'CALLBACK_URL':'http://127.0.0.1:8000/handlepayment/',

                 }
                
                 param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
                 return  render(request, 'paytm.html', {'param_dict': param_dict})
            return render(request,"cart.html")

        # return redirect('store')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})