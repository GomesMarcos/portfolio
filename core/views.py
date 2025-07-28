from django.shortcuts import render

from jobs.views import StackViewSet, get_stack_years, get_worked_years
from social.views import get_social_info


def home(request):
    context = {
        'social_info': get_social_info(request),
        'jobs_years': get_worked_years(),
        'stack_years': get_stack_years(),
        'stack': StackViewSet().queryset,
    }
    return render(request, 'home.html', context)
