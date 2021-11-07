from django import forms

class EmailSendForm(forms.Form):
    to=forms.EmailField()
    msg=forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

