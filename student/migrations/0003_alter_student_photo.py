# Generated by Django 5.1.7 on 2025-07-16 06:57

import student.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=student.models.student_directory_name),
        ),
    ]
