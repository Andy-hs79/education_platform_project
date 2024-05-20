from django.db import models
from users.models import DateTimeMixin, Student, Teacher

# import os
# import sys
#
# sys.path.append(os.path.abspath('../education_platform_project/education_platform'))
# sys.path.append('E:/Andy/_Python/education_platform_project/education_platform')


class Topic(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100, verbose_name="Название раздела")
    index_number = models.IntegerField()
    description = models.TextField()


class Group(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100, verbose_name="Название группы")
    group_teacher = models.ManyToManyField(
        Teacher
    )  # , on_delete=models.SET_NULL, null=True)
    student = models.ManyToManyField(Student)  # , on_delete=models.SET_NULL, null=True)
    # course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)


class Course(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100, verbose_name="Название курса")

    # в курсе несколько разделов
    id_topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # один курс могут проходить несколько групп
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Answer_options(models.Model, DateTimeMixin):
    answer = models.TextField()
    true_answer = models.BooleanField()  # флаг верного ответа


class Questions(models.Model, DateTimeMixin):
    index_number = models.IntegerField()
    id_answer = models.ForeignKey(Answer_options, on_delete=models.SET_NULL, null=True)


# Create your models here.
