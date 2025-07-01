from django.urls import path

from .views import get_job_by_title_or_stack

urlpatterns = [
    path('get_job_by_title_or_stack', get_job_by_title_or_stack, name='get_job_by_title_or_stack'),
]
