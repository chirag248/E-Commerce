from django.shortcuts import render ,redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer

class Otp(View):
    def post(self, request):
        otp = request.POST.get ('otp')
        id = request.POST.get('id')
        print("hello",id)
        message = Customer.Verify(id,otp)
        if message=="Successful":
            print(Customer.objects.filter(id=id).update(is_verified=True))
            return render(request,"login.html",context={"error":message} )
        else:
            return render(request,"otp.html",context= {'error': message} )

class ForgetPassword(View):
    def get(self, request):
        return render(request,"forget.html")
    
    def post(self, request):
        email = request.POST.get('email',None)
        otp = request.POST.get('otp',None)
        password = request.POST.get('password',None)
        if email:
            id=Customer.objects.get(email=email).id
            Customer.Otp(id)
            return render(request,"forgetotp.html",context={"id":id})
        if otp:
            id = request.POST.get('id',None)
            msg = Customer.Verify(id,otp)
            if msg == "Successful":
                return render(request,"forgetpassword.html",context={"id":id})
        if password:
            id = request.POST.get('id',None)
            Customer.objects.filter(id=id).update(password=make_password(password))
            return redirect('login')