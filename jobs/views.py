from django.views.generic import TemplateView

from .models import Job, Stack


class JobView(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    model = Job
    queryset = Job.objects.all().order_by('-time_range__start_date')
    template_name = 'jobs.html'

    def get_context_data(self, **kwargs):
        jobs = self.queryset.only(
            'title', 'start_date', 'end_date', 'description', 'stack', 'is_current_job'
        )
        context = super().get_context_data(**kwargs)
        context['jobs'] = jobs
        return context


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
