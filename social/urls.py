from django.urls import path

from .views import get_social_info

urlpatterns = [
    path('social-info/', get_social_info),
]
