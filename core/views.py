from django.shortcuts import render

from social.views import get_social_info


def home(request):
    context = {'social_info': get_social_info(request)}
    return render(request, 'home.html', context)
