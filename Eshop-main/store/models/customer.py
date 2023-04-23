from django.db import models
import random
from Eshop.settings import EMAIL_HOST_USER
from django.core.mail import send_mail  
from datetime import datetime, timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    updated_at = models.DateTimeField(null=True)

    #to save the data
    def register(self):
        self.save()
        return self.id


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
    def Otp(id):
        otp = random.randint(100000,999999)
        subject = "Greetings"  
        msg = f"Otp for your E-commerce is {otp}"  
        to = Customer.objects.get(id=id).email
        Customer.objects.filter(id=id).update(otp=otp, updated_at=datetime.now())
        send_mail(subject, msg, EMAIL_HOST_USER, [to])

    def Verify(id,otp):
        customer=Customer.objects.get(id=id)
        time_delta = (datetime.now(timezone.utc) - customer.updated_at)
        total_seconds = time_delta.total_seconds()
        minutes = total_seconds/60
        if(minutes<5):
            if(otp==customer.otp):
                return "Successful"
            else:
                return "Invalid Otp"
        else:
            return "Session Expire"

       