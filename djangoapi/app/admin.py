from django.contrib import admin
from .models import Course
# Register your models here.


class CourseDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'language', 'price')


admin.site.register(Course,CourseDataAdmin)     #displays in django-admin
