# Generated by Django 5.0.2 on 2024-04-02 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_process_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processstep',
            name='step_label',
        ),
    ]
