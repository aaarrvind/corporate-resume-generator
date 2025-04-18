from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'designation', 'status', 'professional_summary',
                  'experience', 'education', 'contact_info', 'skills_coding', 'skills_tools', 'projects']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'professional_summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'contact_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'skills_coding': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'skills_tools': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'projects': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }