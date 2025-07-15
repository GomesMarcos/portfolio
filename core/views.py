from django.shortcuts import render

from jobs.views import StackViewSet, get_worked_years
from social.views import get_social_info


def home(request):
    context = {
        'social_info': get_social_info(request),
        'years': get_worked_years(),
        'stack': StackViewSet().queryset,
    }
    return render(request, 'home.html', context)
