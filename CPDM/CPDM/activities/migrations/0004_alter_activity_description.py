# Generated by Django 5.0.2 on 2024-04-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_alter_activity_description_alter_activity_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(),
        ),
    ]
