from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from core.models import TimeRange

# Register your models here.


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(TimeRange)
class TimeRangeAdmin(ModelAdmin):
    list_display = ['display_jobs', 'display_stacks', 'start_date', 'end_date']

    def display_stacks(self, obj):
        return ', '.join([stack.name for stack in obj.stack.all()])

    def display_jobs(self, obj):
        return obj.job.last().title if obj.job.exists() else '-'
