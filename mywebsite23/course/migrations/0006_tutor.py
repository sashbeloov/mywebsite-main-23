# Generated by Django 5.1.4 on 2024-12-25 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
    ]
