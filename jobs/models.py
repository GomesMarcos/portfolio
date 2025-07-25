from functools import cached_property

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import TimeRange


def get_str_time_range(obj):
    return f'from {obj.start_date} to {obj.end_date or "now"}'


class Stack(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True)
    is_current_stack = models.BooleanField(_('Is current stack'), default=True)
    time_range = models.ManyToManyField(TimeRange, verbose_name=_('Time Range'), related_name='stack')
    logo = models.URLField(_('Logo URL'), max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = _('Stack')
        verbose_name_plural = _('Stacks')

    def __str__(self):
        return self.name

    @cached_property
    def get_time_worked(self):
        MONTHS_IN_YEAR = 12
        worked_months_years = {'years': 0, 'months': 0, 'range': []}
        for time_range in self.time_range.all():
            start = time_range.start_date
            end = time_range.end_date or timezone.now().date()
            delta_months = (end.year - start.year) * MONTHS_IN_YEAR + (end.month - start.month)
            if worked_months_years.get('stack') == self.name:
                worked_months_years['years'] += delta_months // MONTHS_IN_YEAR
                worked_months_years['months'] += delta_months % MONTHS_IN_YEAR
            else:
                worked_months_years |= {
                    'stack': self.name,
                    'years': delta_months // MONTHS_IN_YEAR,
                    'months': delta_months % MONTHS_IN_YEAR,
                }
            worked_months_years['range'].append(get_str_time_range(time_range))

        if worked_months_years['months'] >= MONTHS_IN_YEAR:
            calculated_months = worked_months_years['months'] % MONTHS_IN_YEAR
            worked_months_years['years'] += calculated_months + 1
            worked_months_years['months'] = calculated_months

        worked_months_years.pop('stack')
        worked_months_years.pop('range')
        # worked_months_years['range'] = _(', '.join(worked_months_years['range']))

        return worked_months_years

    @cached_property
    def url_logo(self):
        return self.logo


class Job(models.Model):
    title = models.CharField(_('Title'), max_length=50, validators=[MinLengthValidator(2)])
    description = models.TextField(_('Description'), default='')
    url = models.URLField(_('Job URL'), max_length=200, blank=True, null=True)
    logo = models.URLField(_('Company Logo URL'), max_length=500, blank=True, null=True)
    stack = models.ManyToManyField(Stack, verbose_name=_('Stack'))
    is_current_job = models.BooleanField(_('Is Current Job'), default=False)
    time_range = models.ForeignKey(
        TimeRange, verbose_name=_('Time Range'), on_delete=models.PROTECT, related_name='job'
    )

    def __str__(self):
        return self.title

    def clean(self):
        # Se is_current_job for True, end_date deve ser nula
        if self.is_current_job and self.time_range.end_date:
            raise ValidationError(
                {'end_date': _('Se o trabalho é atual, a data de término deve estar vazia.')}
            )

        # Se is_current_job for False, end_date deve ser preenchida
        if not self.is_current_job and not self.time_range.end_date:
            raise ValidationError(
                {'end_date': _('Se o trabalho não é atual, a data de término deve ser preenchida.')}
            )

    @cached_property
    def url_logo(self):
        return self.logo

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')


class Service(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True)
    description = models.TextField(_('Description'), default='')
    url = models.URLField(_('Service URL'), max_length=200, blank=True, null=True)
    url_logo = models.URLField(_('Service Logo URL'), max_length=500, blank=True, null=True)

    jobs = models.ManyToManyField(Job, verbose_name=_('Job'), related_name='service')
    stack = models.ManyToManyField(Stack, verbose_name=_('Stack'), related_name='service')

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
