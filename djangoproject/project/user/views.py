from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.


def home(self):
    
    # we are used here the sql innser join where the both models for the employee and the department
    # the all qurey will be in one qurey
    Employeess = Employee.objects.all().select_related('department')
    emps = {}
    emps_dep = {}
    for emp in Employeess:
        emps[emp.id] = emp.name
        emps_dep[emp.id] = emp.department.name
    print(emps)
    print(emps_dep)
    return HttpResponse("suucees")