# Generated by Django 5.0.4 on 2024-05-12 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education_process", "0001_initial"),
        ("users", "0003_rename_id_user_student_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="group_teacher",
            field=models.ManyToManyField(to="users.teacher"),
        ),
        migrations.AddField(
            model_name="group",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.student",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="id_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="education_process.group",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="id_topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="education_process.topic",
            ),
        ),
        migrations.AlterField(
            model_name="questions",
            name="id_answer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="education_process.answer_options",
            ),
        ),
    ]
