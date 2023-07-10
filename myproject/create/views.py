from django.shortcuts import render
from reg.models import Employee

# Create your views here.
def cre(request):
    return render(request,'create.html')

def details(request):
    employee_id = request.POST['employeeID'];
    first_name = request.POST['firstName'];
    last_name = request.POST['lastName'];
    email = request.POST['email'];
    phone_number = request.POST['phoneNumber'];
    job_id = request.POST['jobID'];
    salary = request.POST['salary'];
    employee = Employee(
          employee_id=employee_id,
          first_name=first_name,
          last_name=last_name,
          email=email,
          phone_number=phone_number,
          job_id=job_id,
          salary=salary
          );
    employee.save();
    return render(request, 'registration.html', {})