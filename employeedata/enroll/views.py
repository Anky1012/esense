from django.shortcuts import render,redirect
from django.views import View
from .forms import EmployeeRegistrationForm
from .models import Employee




def employee_create(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
            return redirect('employee_create')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'app/registration.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'app/employeelist.html', {'employees': employees})


def employee_detail(request,id):
    
    employee = Employee.objects.filter(id=id)
        
    return render(request, 'app/employeedetail.html', {'employee': employee})
