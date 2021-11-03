# from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.
def index_view(request):
    context={"name":"pratik"}
    # print(10/0)
    return TemplateResponse(request, "RevesionMiddlewareApp/index.html" , context)
