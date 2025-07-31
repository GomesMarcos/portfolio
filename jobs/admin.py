from django.contrib import admin

from django.db import models
from unfold.contrib.forms.widgets import WysiwygWidget
from .models import Job, Service, Stack


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_range']
    filter_horizontal = ['stack']

    formfield_overrides = {
        models.TextField: {
            'widget': WysiwygWidget,
        }
    }


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_time_worked']
    filter_horizontal = ['time_range']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_jobs', 'get_stack', 'get_time_worked']
    filter_horizontal = ['jobs', 'stack']

    @admin.display(description='Jobs', ordering='jobs__time_range__end_date')
    def get_jobs(self, obj):
        return ', '.join([job.title for job in obj.jobs.all()])

    @admin.display(description='Stack', ordering='stack__time_range__end_date')
    def get_stack(self, obj):
        return ', '.join([stack.name for stack in obj.stack.all()])

    def get_time_worked(self, obj):
        return obj.get_time_worked['years'], obj.get_time_worked['months']

    get_time_worked.short_description = 'Time Worked'
    get_time_worked.admin_order_field = 'get_time_worked__years'  # Sort by years worked
    get_time_worked.admin_order_field = 'get_time_worked__months'  # Sort by months worked
    get_time_worked.allow_tags = True  # Allow HTML tags in the admin display
    get_time_worked.boolean = True  # Display as boolean in the admin list view
    get_time_worked.admin_order_field = 'get_time_worked'  # Allow sorting by this field
    get_time_worked.admin_order_field = 'get_time_worked__years'  # Sort by years worked
    get_time_worked.admin_order_field = 'get_time_worked__months'  # Sort by months worked
