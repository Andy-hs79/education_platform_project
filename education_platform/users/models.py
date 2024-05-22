from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class DateTimeMixin:
    date_created = models.DateTimeField(auto_now=True, default=timezone.now)
    date_updated = models.DateTimeField(auto_now_add=True, default=timezone.now)


class User(DateTimeMixin, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.email} {self.first_name} {self.last_name}"

    def __repr__(self):
        return self.email


class Student(DateTimeMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # complited_tests = models.ManyToManyField(Complited_tests)

    def __str__(self):
        return self.user.email

    def __repr__(self):
        return self.user.email


class Teacher(DateTimeMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return str(self.user)


# Create your models here.
