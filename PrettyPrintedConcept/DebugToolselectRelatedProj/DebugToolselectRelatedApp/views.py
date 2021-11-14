from django.shortcuts import render,HttpResponse
from .models import Employee,Department
# Create your views here.
def index_view(request):
    Emps=Employee.objects.select_related('department').all()
    for Emp in Emps:
        print(Emp.department)
    # return HttpResponse('<h1 syle="margin:auto;">Select_Related Application</h1>')
    return None
