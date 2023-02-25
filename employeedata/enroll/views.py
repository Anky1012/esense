from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.views import View
from .forms import EmployeeRegistrationForm
from .models import Employee

# Create your views here.
# class EmployeeRegistrationView(View):
#   def get(self,request):
#      form = EmployeeRegistrationForm()
#      return render(request,'app/registration.html',{'form': form}) 
#   def post(self,request):
#       form = EmployeeRegistrationForm(request.POST)
#       # print(form)
#       if form.is_valid():
#          # print(form.is_valid())
#           form.save()
#           form = EmployeeRegistrationForm()
#       return render(request,'app/registration.html',{'form': form})  
  

def home(request):
   return HttpResponse('hello')
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
    # employee =get_object_or_404(Employee, id=id)
    # employee_id = request.GET.get('employee_id')
    employee = Employee.objects.filter(id=id)
    # employee= get_object_or_404(Employee, pk=image_id).image_field
    
    return render(request, 'app/employeedetail.html', {'employee': employee})
