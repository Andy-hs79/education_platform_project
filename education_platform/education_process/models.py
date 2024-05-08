from django.db import models

from education_platform.users.models import Student, Teacher


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела")
    index_number = models.IntegerField()
    description = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы")
    group_teacher = models.ManyToManyField(Teacher, on_delete=models.CASCADE)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    id_creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id_topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE
    )  # в курсе несколько разделов
    id_group = models.ForeignKey(
        Group, on_delete=models.CASCADE
    )  # один курс могут проходить несколько групп


class Answer_options(models.Model):
    answer = models.TextField()
    true_answer = models.BooleanField()  # флаг верного ответа


class Questions(models.Model):
    index_number = models.IntegerField()
    id_answer = models.ForeignKey(Answer_options, on_delete=models.CASCADE)


# Create your models here.
