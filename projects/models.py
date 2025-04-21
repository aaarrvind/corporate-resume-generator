from django.db import models
from django.contrib.auth.models import User
from admin_page.models import Company
from technologies.models import CodingLanguage, Tool

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    technologies = models.ManyToManyField(CodingLanguage, blank=True)
    tools = models.ManyToManyField(Tool, blank=True)
    roles_responsibilities = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Closed', 'Closed')])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_updated')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'