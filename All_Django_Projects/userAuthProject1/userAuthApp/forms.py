from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#creating the model for class
class User_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password",]
        help_text={"username": None }
        widgets={"password":forms.PasswordInput()}
