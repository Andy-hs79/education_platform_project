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


class Specialization(models.Model):
    name = models.CharField(_("Специализация"), max_length=100)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def __repr__(self):
        return f"{self.pk} - {self.name}"


class Student(DateTimeMixin, models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")

    def __str__(self):
        return f"{self.pk} - {self.user.first_name}.{self.user.last_name}"

    def __repr__(self):
        return f"{self.pk} - {self.user.first_name}.{self.user.last_name}"


class Teacher(DateTimeMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(
        Specialization, verbose_name="Специализации"
    )

    def __str__(self):
        return f"{self.pk} - {self.user.first_name}.{self.user.last_name}"

    def __repr__(self):
        return f"{self.pk} - {self.user.first_name}.{self.user.last_name}"


class Group(DateTimeMixin, models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    date_formation = models.DateField(
        verbose_name="Дата образования", default=timezone.now()
    )
    course = models.ForeignKey(
        "education_process.Course", on_delete=models.CASCADE, verbose_name="Курс"
    )
    students = models.ManyToManyField(Student, verbose_name="Студенты")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель"
    )

    @property
    def students_quantity(self):
        return len(self.students.all())

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.date_formation}"
