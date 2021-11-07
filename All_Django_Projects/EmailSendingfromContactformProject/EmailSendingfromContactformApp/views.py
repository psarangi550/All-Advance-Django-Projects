from django.shortcuts import render,HttpResponse
from .forms import EmailSendForm
from django.core.mail import send_mail
from django.urls import reverse
from EmailSendingfromContactformProject import settings
# Create your views here.
def index_view(request):
    if request.method=="POST":
        form=EmailSendForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["to"]
            msg=form.cleaned_data["msg"]
            url=request.build_absolute_uri(request.get_full_path())
            msg+='\n'+str(url)
            send_mail("Email from Pratik",msg,settings.EMAIL_HOST_USER,[email])
            return render(request,"EmailSendingfromContactformApp/email.html",{"name":email})
    form = EmailSendForm()
    return render(request, "EmailSendingfromContactformApp/send_form.html",{"form":form})


