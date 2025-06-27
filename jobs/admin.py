from django.contrib import admin

from .models import Job, Stack


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_range']
    filter_horizontal = ['stack']


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_time_worked']
    filter_horizontal = ['time_range']
