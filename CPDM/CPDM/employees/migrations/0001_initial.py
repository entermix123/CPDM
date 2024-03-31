# Generated by Django 5.0.2 on 2024-03-31 19:52

import CPDM.employees.validators
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0008_alter_company_name'),
        ('departments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, message='First Name must be at least 15 characters long'), CPDM.employees.validators.validate_employee_first_name])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, message='First Name must be at least 15 characters long'), CPDM.employees.validators.validate_employee_last_name])),
                ('title', models.CharField(blank=True, help_text='Enter seniority and position', max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3, message='Title must be at least 3 characters long')])),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('company', models.ManyToManyField(related_name='employees_companies', to='company.company')),
                ('company_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ManyToManyField(related_name='employees_departments', to='departments.department')),
            ],
        ),
    ]