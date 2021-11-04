from django.shortcuts import render

# Create your views here.
def error_404_view(request,exception):
    return render(request, 'Custom404ErrorApp/404.html')
