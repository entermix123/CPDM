# Generated by Django 5.0.2 on 2024-04-02 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 2, 20, 57, 59, 970856, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
