from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")

    def __str__(self):
        return self.email


class Student(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    # complited_tests = models.ManyToManyField(Complited_tests)


class Teacher(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела")
    index_number = models.IntegerField()
    description = models.TextField()


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы")
    id_course = models.OneToOneField(Course, on_delete=models.CASCADE)
    group_teacher = models.ManyToManyField(Teacher, on_delete=models.CASCADE)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Answer_options(models.Model):
    answer = models.TextField()
    true_answer = models.BooleanField()  # флаг верного ответа


class Questions(models.Model):
    index_number = models.IntegerField()
    id_answer = models.ForeignKey(Answer_options, on_delete=models.CASCADE)


# Create your models here.
