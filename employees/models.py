from django.db import models
from django.contrib.auth.models import User
from admin_page.models import Company
from technologies.models import CodingLanguage, Tool
from projects.models import Project

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('SE', 'Software Engineer'),
        ('PM', 'Project Manager'),
        ('DE', 'Data Engineer'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    full_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    status = models.CharField(max_length=20, choices=[('Current', 'Current'), ('Ex', 'Ex')])
    professional_summary = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    contact_info = models.TextField(blank=True)
    skills_coding = models.ManyToManyField(CodingLanguage, blank=True)
    skills_tools = models.ManyToManyField(Tool, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='employee_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='employee_updated')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'employee'