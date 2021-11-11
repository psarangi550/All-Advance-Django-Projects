from django.shortcuts import render,redirect
from .models import Movie,Character
from django.forms import inlineformset_factory #importing the inlineformset factory
# Create your views here.
def index_view(request,id):
    movie=Movie.objects.get(pk=id)
    Charformset=inlineformset_factory(Movie,Character,fields=('name',),extra=1)

    if request.method=="POST":
        form=Charformset(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index' , id=movie.id)
    form=Charformset(instance=movie)

    context={"form":form}
    return render(request, "inlineformsetApp/index.html" , context)

