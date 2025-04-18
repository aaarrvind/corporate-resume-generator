from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Project
from .forms import ProjectForm
from admin_page.models import Company
from technologies.models import CodingLanguage, Tool

@login_required
def project_list(request):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'projects/error.html', {'message': 'No company available'})
        active_projects = Project.objects.filter(is_deleted=False, company=company)
        deleted_projects = Project.objects.filter(is_deleted=True, company=company)
    except Company.DoesNotExist:
        active_projects = Project.objects.none()
        deleted_projects = Project.objects.none()
    return render(request, 'projects/project_list.html', {
        'active_projects': active_projects,
        'deleted_projects': deleted_projects
    })

@login_required
def project_create(request):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'projects/error.html', {'message': 'No company available'})
    except Company.DoesNotExist:
        return render(request, 'projects/error.html', {'message': 'No company assigned'})
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            try:
                project = form.save(commit=False)
                project.company = company
                project.created_by = request.user
                project.updated_by = request.user
                project.save()
                form.save_m2m()
                return redirect('project_list')
            except IntegrityError:
                form.add_error('name', 'This name already exists. Check deleted projects to restore or permanently delete.')
    else:
        form = ProjectForm()
    no_techs = not CodingLanguage.objects.filter(is_deleted=False).exists()
    no_tools = not Tool.objects.filter(is_deleted=False).exists()
    return render(request, 'projects/project_form.html', {
        'form': form,
        'no_techs': no_techs,
        'no_tools': no_tools
    })

@login_required
def project_update(request, pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'projects/error.html', {'message': 'No company available'})
        project = get_object_or_404(Project, pk=pk, is_deleted=False, company=company)
    except Company.DoesNotExist:
        return render(request, 'projects/error.html', {'message': 'No company assigned'})
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.updated_by = request.user
            project.save()
            form.save_m2m()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    no_techs = not CodingLanguage.objects.filter(is_deleted=False).exists()
    no_tools = not Tool.objects.filter(is_deleted=False).exists()
    return render(request, 'projects/project_form.html', {
        'form': form,
        'no_techs': no_techs,
        'no_tools': no_tools
    })

@login_required
def project_delete(request, pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'projects/error.html', {'message': 'No company available'})
        project = get_object_or_404(Project, pk=pk, is_deleted=False, company=company)
    except Company.DoesNotExist:
        return render(request, 'projects/error.html', {'message': 'No company assigned'})
    project.is_deleted = True
    project.updated_by = request.user
    project.save()
    return redirect('project_list')

@login_required
def project_restore(request, pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'projects/error.html', {'message': 'No company available'})
        project = get_object_or_404(Project, pk=pk, is_deleted=True, company=company)
    except Company.DoesNotExist:
        return render(request, 'projects/error.html', {'message': 'No company assigned'})
    project.is_deleted = False
    project.updated_by = request.user

    project.save()
    return redirect('project_list')

@login_required
def project_permanent_delete(request, pk):
    try:
        company = Company.objects.first()
        if not company:
            return render(request, 'projects/error.html', {'message': 'No company available'})
        project = get_object_or_404(Project, pk=pk, is_deleted=True, company=company)
    except Company.DoesNotExist:
        return render(request, 'projects/error.html', {'message': 'No company assigned'})
    project.delete()
    return redirect('project_list')