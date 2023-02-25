
from django import forms
from.models import *




class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'lastname', 'email','phoneNo','address', 'designation', 'employee_image']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'lastname':forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'}),
        'phoneNo':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'designation':forms.Select(attrs={'class':'form-control'}),
        # 'employee_image':forms.ImageField(attrs={'class':'form-control'}),

       
        }