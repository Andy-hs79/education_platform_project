from django.db import models
from django.utils import timezone
from users.models import Student, Teacher


class DateTimeMixin:
    date_created = models.DateTimeField(auto_now=True, default=timezone.now)
    date_updated = models.DateTimeField(auto_now_add=True, default=timezone.now)


class Topic(DateTimeMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела")
    index_number = models.IntegerField()
    description = models.TextField()


class Group(DateTimeMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы")
    group_teacher = models.ManyToManyField(
        Teacher
    )  # , on_delete=models.SET_NULL, null=True)
    student = models.ManyToManyField(Student)  # , on_delete=models.SET_NULL, null=True)
    # course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)


class Course(DateTimeMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")

    # в курсе несколько разделов
    id_topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # один курс могут проходить несколько групп
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Answer_options(DateTimeMixin, models.Model):
    answer = models.TextField()
    true_answer = models.BooleanField()  # флаг верного ответа


class Questions(DateTimeMixin, models.Model):
    index_number = models.IntegerField()
    id_answer = models.ForeignKey(Answer_options, on_delete=models.SET_NULL, null=True)


# Create your models here.


class Tests(DateTimeMixin,models.Model):
    name = models.CharField(max_length=100, verbose_name="Название теста")
   # test
    discription = models.TextField()
    index = models.IntegerField()
    timelemit = models.DateTimeField()
    questions = models.ForeignKey(Questions, on_delete=models.SET_NULL, null=True)

class Complited_Tests(DateTimeMixin,models.Model):
    iscomplited = models.BooleanField()
    test = models.OneToOneField(Tests)

class Recuered_test():