# Generated by Django 5.1.4 on 2024-12-18 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='slug',
        ),
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]
