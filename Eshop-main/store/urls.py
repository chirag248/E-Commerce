from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart, delete
from .views.checkout import CheckOut, handlerequest
from .views.orders import OrderView
from .views.product import Product
from .views.otp import Otp, ForgetPassword
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('forgot-password', ForgetPassword.as_view(), name='fp'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('otp-verification', Otp.as_view() , name='otp'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product-detail/<int:id>', Product.as_view(), name='product'),
    path("handlerequest/",handlerequest, name="HandleRequest"),
    path("delete/<str:id>",delete, name="Delete"),


]
