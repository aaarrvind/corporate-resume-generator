from django import forms
from .models import Project
from technologies.models import CodingLanguage, Tool
from employees.models import Employee

class ProjectForm(forms.ModelForm):
    technologies = forms.ModelMultipleChoiceField(
        queryset=CodingLanguage.objects.filter(is_deleted=False),
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect'}),
        required=False
    )
    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.filter(is_deleted=False),
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect'}),
        required=False
    )
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.filter(is_deleted=False),
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect'}),
        required=False
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'technologies', 'tools', 'roles_responsibilities',
                  'start_date', 'end_date', 'status', 'employees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'roles_responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }