from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Address, PhoneNumber, Social, SocialMedia


@admin.register(Address)
class AddressAdmin(ModelAdmin): ...


@admin.register(PhoneNumber)
class PhoneNumberAdmin(ModelAdmin): ...


@admin.register(Social)
class SocialAdmin(ModelAdmin): ...


@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin): ...
