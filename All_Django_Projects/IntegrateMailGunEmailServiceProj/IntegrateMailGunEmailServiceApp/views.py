from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index_view(request):
    send_mail("Hello","This is a Test" ,"pratik.django@gmail.com", ["psarangi58@gmail.com"])
    return render(request, "IntegrateMailGunEmailServiceApp/index.html")
