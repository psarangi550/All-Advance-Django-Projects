from django.shortcuts import render,redirect
from .models import Location
# Create your views here.
from django.forms import modelformset_factory

def index_view(request):
    formset=modelformset_factory(Location, fields=("name","loc"))
    if request.method == "POST":
        locationform=formset(request.POST)
        if locationform.is_valid():
            locationform.save()
            return redirect("index")

    locationform=formset()
    return render( request, 'modelformsetapp/index.html',{"form":locationform})
