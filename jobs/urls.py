from django.urls import path

from .views import StackViewSet, get_job_by_title_or_stack, get_job_details, get_jobs_by_stack

urlpatterns = [
    path('get_job_by_title_or_stack', get_job_by_title_or_stack, name='get_job_by_title_or_stack'),
    path('get_job_details/<int:job_id>/', get_job_details, name='get_job_details'),
    path('get_jobs_by_stack/<int:stack_id>/', get_jobs_by_stack, name='get_jobs_by_stack'),
    path('stack/', StackViewSet.as_view()),
]
