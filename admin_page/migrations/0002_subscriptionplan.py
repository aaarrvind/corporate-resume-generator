# Generated by Django 4.2.19 on 2025-04-22 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10)),
                ('duration_days', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('offer_details', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
