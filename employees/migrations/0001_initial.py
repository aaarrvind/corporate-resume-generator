# Generated by Django 5.2 on 2025-04-18 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_page', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('designation', models.CharField(choices=[('SE', 'Software Engineer'), ('PM', 'Project Manager'), ('DE', 'Data Engineer')], max_length=100)),
                ('status', models.CharField(choices=[('Current', 'Current'), ('Ex', 'Ex')], max_length=20)),
                ('professional_summary', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('contact_info', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='admin_page.company')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
