from django.shortcuts import render

# Create your views here.
def index_view(request):
    context={"name":"pratik"}
    return render(request, "templatefragmentcacheApp/index.html",context)
