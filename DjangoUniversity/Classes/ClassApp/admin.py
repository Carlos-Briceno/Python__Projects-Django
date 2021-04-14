from django.contrib import admin

from .models import djangoClasses
from .models import studentNames
from .models import schedule


admin.site.register(djangoClasses)
admin.site.register(studentNames)
admin.site.register(schedule)
