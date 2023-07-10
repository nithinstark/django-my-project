from django.shortcuts import render
from .models import Employee

# Create your views here.
def reg(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request,'registration.html', context)
