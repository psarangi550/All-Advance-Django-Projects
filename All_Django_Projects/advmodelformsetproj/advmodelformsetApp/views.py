from django.shortcuts import render,redirect
from django.forms import modelformset_factory
from .models import Programmer,Language
# Create your views here.

def index_view(request,id):
    programmer=Programmer.objects.get(id=id)
    language_formset=modelformset_factory(Language, extra=2, fields=("name",))
    if request.method=="POST":
        formset=language_formset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        instances = formset.save(commit=False)
        for instance in instances:
            instance.programmer_id=programmer.id
            instance.save()
        return redirect ("home",id=programmer.id)
    formset=language_formset(queryset=Language.objects.filter(programmer__id=programmer.id))
    return render(request, "advmodelformsetApp/index.html", {"form":formset})
