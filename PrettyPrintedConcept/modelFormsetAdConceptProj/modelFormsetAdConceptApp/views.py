from django.shortcuts import render
from django.forms import modelformset_factory as modelformset_factory
#importing the model Formset Factory
from .models import Employee
# Create your views here.
def index_view(request):
    EmpFormSet=modelformset_factory(Employee,fields=("eno","ename","esal","eaddr"),extra=2)
    if request.method == "POST":
        form=EmpFormSet(request.POST)
        if form.is_valid():
            form.save()
    form=EmpFormSet(queryset=Employee.objects.filter(eno=101))
    context={"form":form}
    return render(request, "modelFormsetAdConceptApp/index.html", context)
