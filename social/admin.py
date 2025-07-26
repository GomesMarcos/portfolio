from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget


from .models import Address, PhoneNumber, Social, SocialMedia


@admin.register(Address)
class AddressAdmin(ModelAdmin): ...


@admin.register(PhoneNumber)
class PhoneNumberAdmin(ModelAdmin): ...


@admin.register(Social)
class SocialAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin): ...
