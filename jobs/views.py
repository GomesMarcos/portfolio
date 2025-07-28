from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .models import Job, Stack


def get_worked_years():
    """
    Returns a list of unique years (descending) in which jobs have a start date.

    Returns:
        list: List of years (int) ordered from most recent to oldest.
    """
    years = list(
        Job.objects.values_list('time_range__start_date__year', flat=True)
        .distinct()
        .order_by('-time_range__start_date__year')
    )
    years += list(
        Job.objects.values_list('time_range__end_date__year', flat=True)
        .distinct()
        .order_by('-time_range__end_date__year')
    )
    return set(years)


def get_stack_years():
    """
    Returns a list of unique years (descending) in which stacks have been used.

    Returns:
        list: List of years (int) ordered from most recent to oldest.
    """
    return {stack.get_time_worked['years'] for stack in Stack.objects.all()}


@require_POST
@csrf_exempt
def get_job_by_title_or_stack(request):
    """
    Handles job search/filter requests by title, stack, or year.
    Returns a rendered HTML partial with the filtered jobs and available years.

    Args:
        request: The HTTP request object containing search and year parameters.

    Returns:
        HttpResponse: Rendered HTML with filtered jobs and year filter buttons.
    """
    query = request.POST.get('search', '')
    year = request.POST.get('year', '')

    jobs = (
        Job.objects.filter(title__icontains=query)
        | Job.objects.filter(stack__name__icontains=query)
        | Job.objects.filter(time_range__start_date__icontains=query)
        | Job.objects.filter(time_range__end_date__icontains=query)
    )
    jobs = jobs.distinct().order_by('-time_range__start_date')
    # Filtro por ano, se fornecido
    if year:
        jobs = jobs.filter(time_range__start_date__year=year) | jobs.filter(time_range__end_date__year=year)

    html = render_to_string('partials/job_search_results.html', {'jobs': jobs})
    return HttpResponse(html)


def get_job_details(request, job_id):
    job = Job.objects.get(pk=job_id)
    html = render_to_string('partials/job_details.html', {'job': job})
    return HttpResponse(html)


def get_jobs_by_stack(request, stack_id):
    jobs = Job.objects.filter(stack=stack_id).order_by('-time_range__start_date')
    html = render_to_string('partials/job_search_results.html', {'jobs': jobs})
    return HttpResponse(html)


class StackViewSet(TemplateView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    model = Stack
    queryset = Stack.objects.all().order_by('name', 'is_current_stack')
    template_name = 'sections/stack.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stack'] = self.queryset
        return context

    @require_POST
    @csrf_exempt
    def get_stack_by_name_or_worked_years(query):
        stack_search = query.POST.get('stack_search', '')
        current = query.POST.get('current', False)
        worked_years = query.POST.get('worked_years', '')

        stack = Stack.objects.all().order_by('name')

        if stack_search:
            stack = stack.filter(name__icontains=stack_search)
        if worked_years.isdigit():
            # Filtering by get_time_worked with Python 'cause it's not in DB
            stack = [s for s in stack if str(s.get_time_worked['years']) == str(worked_years)]

        return HttpResponse(render_to_string('partials/stack_search_result.html', {'stack': stack}))
