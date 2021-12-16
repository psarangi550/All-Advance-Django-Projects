from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.models import User
class EmpCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields=("username","password1","password2",)

class EmpAuthForm(AuthenticationForm):
    username=UsernameField()
    password=forms.CharField(widget=forms.PasswordInput)



