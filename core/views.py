from django.shortcuts import render

from social.views import get_social_info


def home(request):
    social_info = get_social_info(request)
    context = {'social_info': social_info}
    return render(request, 'home.html', context)
