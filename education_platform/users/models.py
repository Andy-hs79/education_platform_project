from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# import os
# import sys
# sys.path.append(os.path.abspath('../education_platform_project/education_platform'))
# sys.path.append('E:/Andy/_Python/education_platform_project')

# from education_process.models import Course


class DateTimeMixin:
    date_created = models.DateTimeField(auto_now=True, default=timezone.now)
    date_updated = models.DateTimeField(auto_now_add=True, default=timezone.now)


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    REQUIRED_FIELDS = [first_name, last_name]

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


class Student(models.Model, DateTimeMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # complited_tests = models.ManyToManyField(Complited_tests)

    def __str__(self):
        return self.user

    def __repr__(self):
        return self.user


class Teacher(models.Model, DateTimeMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def __repr__(self):
        return self.user


# Create your models here.
