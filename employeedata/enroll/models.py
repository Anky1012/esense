from django.db import models

# Create your models here.


DESIGNATION_CHOICES =(('Manager','Manager'),
                      ('Developer','Developer'),
                      ('Tester','Tester'),
)
class Employee(models.Model):
    
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNo = models.CharField(max_length=10)
    address =models.TextField()
    designation = models.CharField(choices = DESIGNATION_CHOICES, max_length=200)
    
    employee_image = models.ImageField(upload_to = 'employeeimg/', null=True, blank=True)
    
    # def __str__(self):
    #     return f"{self.name}  {self.lastname}  {self.email}  {self.phoneNo}  {self.address}  {self.employee_image}"

    def __str__(self):
        return str(self.id)