from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .models import Job, Stack


@require_POST
@csrf_exempt
def get_job_by_title_or_stack(request):
    query = request.POST.get('search', '')
    jobs = Job.objects.filter(title__icontains=query) | Job.objects.filter(
        stack__name__icontains=query
    )
    jobs = jobs.distinct().order_by('-time_range__start_date')
    html = render_to_string('partials/job_search_results.html', {'jobs': jobs})
    return HttpResponse(html)


class StackViewSet(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Stack.objects.all().order_by('is_current_stack')


class StackTimeRangeViewSet(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = (
        Stack.objects.prefetch_related('time_range')
        .values('time_range')
        .order_by('-time_range__start_date')
    )
