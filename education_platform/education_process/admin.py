from django.contrib import admin

from .models import Course, Topic, Test, Question, Answer, Article, CompletedTest


admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Article)
admin.site.register(CompletedTest)
