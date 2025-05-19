from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import CodingLanguage, Tool
from .forms import CodingLanguageForm, ToolForm

# @login_required
def coding_language_list(request):
    active_languages = CodingLanguage.objects.filter(is_deleted=False)
    deleted_languages = CodingLanguage.objects.filter(is_deleted=True)
    return render(request, 'technologies/coding_language_list.html', {
        'active_languages': active_languages,
        'deleted_languages': deleted_languages
    })

# @login_required
def coding_language_create(request):
    if request.method == 'POST':
        form = CodingLanguageForm(request.POST)
        if form.is_valid():
            try:
                language = form.save(commit=False)
                language.created_by = request.user
                language.updated_by = request.user
                language.save()
                return redirect('coding_language_list')
            except IntegrityError:
                form.add_error('name', 'This name already exists. Check deleted records to restore or permanently delete.')
    else:
        form = CodingLanguageForm()
    return render(request, 'technologies/coding_language_form.html', {'form': form})

# @login_required
def coding_language_update(request, pk):
    language = get_object_or_404(CodingLanguage, pk=pk, is_deleted=False)
    if request.method == 'POST':
        form = CodingLanguageForm(request.POST, instance=language)
        if form.is_valid():
            try:
                language = form.save(commit=False)
                language.updated_by = request.user
                language.save()
                return redirect('coding_language_list')
            except IntegrityError:
                form.add_error('name', 'This name already exists.')
    else:
        form = CodingLanguageForm(instance=language)
    return render(request, 'technologies/coding_language_form.html', {'form': form})

# @login_required
def coding_language_delete(request, pk):
    language = get_object_or_404(CodingLanguage, pk=pk, is_deleted=False)
    language.is_deleted = True
    language.updated_by = request.user
    language.save()
    return redirect('coding_language_list')

# @login_required
def coding_language_restore(request, pk):
    language = get_object_or_404(CodingLanguage, pk=pk, is_deleted=True)
    language.is_deleted = False
    language.updated_by = request.user
    language.save()
    return redirect('coding_language_list')

# @login_required
def coding_language_permanent_delete(request, pk):
    language = get_object_or_404(CodingLanguage, pk=pk, is_deleted=True)
    language.delete()
    return redirect('coding_language_list')

# @login_required
def tool_list(request):
    active_tools = Tool.objects.filter(is_deleted=False)
    deleted_tools = Tool.objects.filter(is_deleted=True)
    return render(request, 'technologies/tool_list.html', {
        'active_tools': active_tools,
        'deleted_tools': deleted_tools
    })

# @login_required
def tool_create(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            try:
                tool = form.save(commit=False)
                tool.created_by = request.user
                tool.updated_by = request.user
                tool.save()
                return redirect('tool_list')
            except IntegrityError:
                form.add_error('name', 'This name already exists. Check deleted records to restore or permanently delete.')
    else:
        form = ToolForm()
    return render(request, 'technologies/tool_form.html', {'form': form})

# @login_required
def tool_update(request, pk):
    tool = get_object_or_404(Tool, pk=pk, is_deleted=False)
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            try:
                tool = form.save(commit=False)
                tool.updated_by = request.user
                tool.save()
                return redirect('tool_list')
            except IntegrityError:
                form.add_error('name', 'This name already exists.')
    else:
        form = ToolForm(instance=tool)
    return render(request, 'technologies/tool_form.html', {'form': form})

# @login_required
def tool_delete(request, pk):
    tool = get_object_or_404(Tool, pk=pk, is_deleted=False)
    tool.is_deleted = True
    tool.updated_by = request.user
    tool.save()
    return redirect('tool_list')

# @login_required
def tool_restore(request, pk):
    tool = get_object_or_404(Tool, pk=pk, is_deleted=True)
    tool.is_deleted = False
    tool.updated_by = request.user
    tool.save()
    return redirect('tool_list')

# @login_required
def tool_permanent_delete(request, pk):
    tool = get_object_or_404(Tool, pk=pk, is_deleted=True)
    tool.delete()
    return redirect('tool_list')