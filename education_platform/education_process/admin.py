from django.contrib import admin

from .models import Answer_options, Course, Group, Questions, Topic

admin.site.register(Topic)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Answer_options)
admin.site.register(Questions)

# Register your models here.
