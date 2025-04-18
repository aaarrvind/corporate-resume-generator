from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm
from admin_page.models import Company
from technologies.models import CodingLanguage, Tool
from projects.models import Project

@login_required
def employee_list(request):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'employees/error.html', {'message': 'No company available'})
        employees = Employee.objects.filter(is_deleted=False, company=company)
    except Company.DoesNotExist:
        employees = Employee.objects.none()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'employees/error.html', {'message': 'No company available'})
    except Company.DoesNotExist:
        return render(request, 'employees/error.html', {'message': 'No company assigned'})
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.created_by = request.user
            employee.updated_by = request.user
            employee.save()
            form.save_m2m()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    no_techs = not CodingLanguage.objects.filter(is_deleted=False).exists()
    no_tools = not Tool.objects.filter(is_deleted=False).exists()
    no_projects = not Project.objects.filter(is_deleted=False, company=company).exists()
    return render(request, 'employees/employee_form.html', {
        'form': form,
        'no_techs': no_techs,
        'no_tools': no_tools,
        'no_projects': no_projects
    })

@login_required
def employee_update(request, pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'employees/error.html', {'message': 'No company available'})
        employee = get_object_or_404(Employee, pk=pk, is_deleted=False, company=company)
    except Company.DoesNotExist:
        return render(request, 'employees/error.html', {'message': 'No company assigned'})
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.updated_by = request.user
            employee.save()
            form.save_m2m()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    no_techs = not CodingLanguage.objects.filter(is_deleted=False).exists()
    no_tools = not Tool.objects.filter(is_deleted=False).exists()
    no_projects = not Project.objects.filter(is_deleted=False, company=company).exists()
    return render(request, 'employees/employee_form.html', {
        'form': form,
        'no_techs': no_techs,
        'no_tools': no_tools,
        'no_projects': no_projects
    })

@login_required
def employee_delete(request, pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'employees/error.html', {'message': 'No company available'})
        employee = get_object_or_404(Employee, pk=pk, is_deleted=False, company=company)
    except Company.DoesNotExist:
        return render(request, 'employees/error.html', {'message': 'No company assigned'})
    employee.is_deleted = True
    employee.updated_by = request.user
    employee.save()
    return redirect('employee_list')

@login_required
def employee_restore(request, pk):
    try:
        company = Company.objects.filter
        if not company:
            return render(request, 'emplyees/error.html', {'message' : 'No company available'})
        employee = get_object_or_404(Employee, pk=pk, is_deleted = True, company=company)
    except Company.DoesNotExist:
        return render(request, 'employees/error.html', {'message' : 'No company assigned'})
    employee.is_deleted = False
    employee.updated_by = request.user
    employee.save()

    return redirect('employee_list')


@login_required
def employee_permanent_delete(request , pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'employee/error.html', {'message' : 'No company available'})
        employee = get_object_or_404(Employee, pk=pk, is_deleted = True, company = company)
    except Company.DoesNotExist:
        return render(request, 'employee/error.html', {'message':'No company assigned'})
    employee.delete()
    return redirect('employee_list')
