from django import forms
from .models import CodingLanguage, Tool

class CodingLanguageForm(forms.ModelForm):
    class Meta:
        model = CodingLanguage
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}