from django.contrib import admin

# Register your models here.
from .models import Employee

@admin.register(Employee)
# admin.site.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
 list_display=['id','name','lastname','email','phoneNo','address','designation','employeetype']

