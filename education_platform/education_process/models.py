from django.db import models
from users.models import DateTimeMixin, Specialization, Student, Teacher


class Course(DateTimeMixin, models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    duration = models.DurationField(verbose_name="Продолжительность")
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Topic(DateTimeMixin, models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Test(DateTimeMixin, models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Тема")

    def __str__(self):
        return f"Test #{self.pk} - {self.title}"


class Question(DateTimeMixin, models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    text = models.TextField(verbose_name="Текст вопроса")
    difficulty = models.CharField(
        max_length=6, choices=DIFFICULTY_CHOICES, verbose_name="Сложность"
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")

    def __str__(self):
        return f"{self.pk} - {self.text} - {self.difficulty}"


class Answer(DateTimeMixin, models.Model):
    title = models.CharField(max_length=100, verbose_name="Ответ")
    is_correct = models.BooleanField(verbose_name="Верный ответ")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Article(DateTimeMixin, models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    specializations = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"{self.pk} - {self.title}"


class CompletedTest(DateTimeMixin, models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.test}"
