# Generated by Django 5.0.4 on 2024-06-10 17:49

import django.db.models.deletion
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education_process", "0001_add_course_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="education_process.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            bases=(users.models.DateTimeMixin, models.Model),
        ),
    ]
