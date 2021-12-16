from django.shortcuts import render
from .models import Language,Programmer
from django.forms import inlineformset_factory
# Create your views here.

def index_view(request,id):
    programmer=Programmer.objects.get(id=id)
    lang_formset=inlineformset_factory(Programmer, Language, fields=("name",))
    if request.method=="POST":
        form=lang_formset(request.POST, instance=programmer)
        if form.is_valid():
            form.save()
    form=lang_formset(instance=programmer)
    return render(request, "inlineformsetApp/index.html" , {"form":form})
