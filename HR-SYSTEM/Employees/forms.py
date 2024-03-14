from Employees.models import Employee
from Employees.models import Employee
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['FullName', 'Email', 'Emp_code', 'MobileNumber', 'Position']

