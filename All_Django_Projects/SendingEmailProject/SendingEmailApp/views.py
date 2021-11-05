from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index_view(request):
    send_mail("Hello","This is Test","pratik.django@gmail.com" ,["psarangi50@gmail.com"],fail_silently=False)
    return HttpResponse("<h1>Email Sent</h1>")
