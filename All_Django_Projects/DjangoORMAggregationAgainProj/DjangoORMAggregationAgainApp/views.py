from django.shortcuts import render,HttpResponse
from .models import Employee
from django.db.models import Count
# Create your views here.

def index_view(request):
    emp_count=Employee.objects.aggregate(Count("esal"))
    return HttpResponse('emp count is {}'.format(emp_count["esal__count"]))
