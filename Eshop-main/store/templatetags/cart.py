from django import template

from store.models.product import Products

register = template.Library ()



@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if id == product:
            return cart.get (id)
    return 0;


@register.filter (name='price_total')
def price_total(product, cart):
    prod=Products.objects.get(id=int(product.split("_")[0]))
    return prod.price * cart_quantity (product, cart)


@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0;
    for p in products:
        
        sum += price_total (p['prod'], cart)

    return sum
