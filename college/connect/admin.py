from django.contrib import admin

# # Register your models here.

from .models import *

admin.site.register(Project)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Research)
admin.site.register(Project_Student)
admin.site.register(Project_Teacher)
admin.site.register(Research_Teacher)