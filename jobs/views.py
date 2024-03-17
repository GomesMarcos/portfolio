from django.views.generic import TemplateView

from .models import Job, Stack, StackTimeRange


class JobView(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Job.objects.all().order_by('-start_date')
    template_name = 'jobs.html'


class StackViewSet(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Stack.objects.all().order_by('is_current_stack')


class StackTimeRangeViewSet(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = StackTimeRange.objects.all().order_by('-start_date')
