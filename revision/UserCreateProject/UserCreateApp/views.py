from django.shortcuts import render,HttpResponseRedirect
from .forms import EmpCreationForm,EmpAuthForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def index_view(request):
    if request.method=="POST":
        form=EmpCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registration Successful")
            form=EmpCreationForm()
    else:
        form=EmpCreationForm()
    return render(request, "UserCreateApp/index.html" , {"form":form})

def login_user_view(request):
    if request.method=="POST":
        form=EmpAuthForm(request.user,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user=request.user)
                # update_session_auth_hash(form)
                return HttpResponseRedirect("/admin/")
    form=EmpAuthForm()
    return render(request, "UserCreateApp/login.html" , {"form":form})


