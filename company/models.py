from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    subscription_plan = models.CharField(max_length=100)
    usage_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.company_name
