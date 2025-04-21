from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CodingLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='coding_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='coding_updated')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta: 
        db_table = 'coding_language'


class Tool(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tool_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tool_updated')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta: 
        db_table = 'tool'
