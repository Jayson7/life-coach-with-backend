from django.shortcuts import render
from .models import forms
from django.core.mail import send_mail
# Create your views here.

# myaccount.google.com/lesssecureapps
    
def home(request):
    if request.method == 'POST':
        subject = request.POST['Subject']
        email = request.POST['Email']
        message = request.POST['Message']
        name = request.POST['Name']
        send_mail(
                subject,
               
                message,
                email,
                ["omobolaji520@gmail.com"],
                fail_silently = True,
                )


        former = forms(subject = subject, email = email, message = message, name= name)
        former.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
   
    return render(request, 'index.html')

def payment(request):
    return render(request, 'payment.html')
