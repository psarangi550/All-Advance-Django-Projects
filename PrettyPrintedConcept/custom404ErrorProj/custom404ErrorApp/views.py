from django.shortcuts import render,HttpResponse

# Create your views here.
def error_404_view(request,exception):
    return HttpResponse("<h1>Error Page<h1>")
