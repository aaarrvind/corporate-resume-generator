from django import forms
from .models import Employee
from technologies.models import CodingLanguage, Tool
from projects.models import Project

class EmployeeForm(forms.ModelForm):
    skills_coding = forms.ModelMultipleChoiceField(
        queryset=CodingLanguage.objects.filter(is_deleted=False),
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect'}),
        required=False
    )
    skills_tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.filter(is_deleted=False),
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect'}),
        required=False
    )
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.filter(is_deleted=False),
        widget=forms.SelectMultiple(attrs={'class': 'form-control multiselect'}),
        required=False
    )

    class Meta:
        model = Employee
        fields = ['full_name', 'designation',  'status', 'skills_coding', 'skills_tools', 'projects']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }