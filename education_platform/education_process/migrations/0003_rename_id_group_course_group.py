# Generated by Django 5.0.4 on 2024-05-13 06:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("education_process", "0002_group_group_teacher_group_student_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="id_group",
            new_name="group",
        ),
    ]
