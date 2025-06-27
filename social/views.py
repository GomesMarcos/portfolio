from .models import Social

# Create your views here.


def get_social_info(request):
    return Social.objects.last()
