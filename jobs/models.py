from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


def validate_is_current(date):
    return not bool(date)


def set_is_current_by_end_date(end_date):
    return not bool(end_date)


def get_str_time_range(obj):
    return f"( from {obj.start_date} to {obj.end_date or 'now'})"


class Stack(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    is_current_stack = models.BooleanField(_("Is current stack"), default=True)

    # is_current_stack = models.BooleanField(_("Is Current Stack"),
    #    default=set_is_current_by_end_date(time_range[-1].end_date))

    def __str__(self):
        return self.name

    @property
    def get_time_worked(self):
        MONTHS_IN_YEAR = 12
        worked_months_years = {}
        for time_range in self.time_range.all():
            start = time_range.start_date
            end = time_range.end_date or timezone.now().date()
            delta_months = (end.year - start.year) * MONTHS_IN_YEAR + (end.month - start.month)
            worked_months_years |= {
                "years": (delta_months % MONTHS_IN_YEAR) - 1,
                "months": int(delta_months / MONTHS_IN_YEAR),
                "range": get_str_time_range(time_range),
            }
        return worked_months_years


class StackTimeRange(models.Model):
    start_date = models.DateField(_("Start Date"), validators=[MaxValueValidator(timezone.now().date())])
    end_date = models.DateField(
        _("End Date"),
        validators=[MinValueValidator(start_date)],
        blank=True,
        null=True,
    )
    stack = models.ForeignKey(
        Stack,
        verbose_name=_("Stack"),
        related_name="time_range",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.stack.name} {get_str_time_range(self)}"


class Job(models.Model):
    title = models.CharField(_("Title"), max_length=50, validators=[MinLengthValidator(2)])
    start_date = models.DateField(
        _("Start Date"),
        validators=[MaxValueValidator(timezone.now().date())],
    )
    end_date = models.DateField(
        _("End Date"),
        validators=[MinValueValidator(start_date), MaxValueValidator(timezone.now().date())],
        blank=True,
        null=True,
    )
    description = models.TextField(_("Description"), default='')
    url = models.URLField(_("Job URL"), max_length=200)
    logo = models.URLField(_("Job Logo"), max_length=500, blank=True, null=True)
    stack = models.ManyToManyField(Stack, verbose_name=_("Stack"))
    is_current_job = models.BooleanField(_("Is Current Job"), default=validate_is_current(end_date))

    def __str__(self):
        return self.title
