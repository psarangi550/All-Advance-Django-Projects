from django.shortcuts import render,redirect
from .models import Movie,Character
from django.forms import modelformset_factory
# Create your views here.
def imdex_view(request,pk):#defining the view function
    movie=Movie.objects.get(pk=pk)
    CharFormSet=modelformset_factory(Character, extra=2, fields=('name',))
    if request.method=="POST":
        form=CharFormSet(request.POST, queryset=Character.objects.filter(movie__id=movie.id))
        if form.is_valid():
            chars=form.save(commit=False)
            for char in chars :
                char.movie=movie
                char.save()
                return redirect("index",pk=movie.id)
    form=CharFormSet(queryset=Character.objects.filter(movie__id=movie.id))
    context={"form":form}
    return render(request,"ComplexModelFormsetApp/index.html", context)

