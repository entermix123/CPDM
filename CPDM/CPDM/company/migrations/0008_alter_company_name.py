# Generated by Django 5.0.2 on 2024-03-31 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(error_messages={'unique': 'Company with this name already exists. Choose another one'}, max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Cannot have less than 3 characters')]),
        ),
    ]
