from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeRange(models.Model):
    start_date = models.DateField(
        _('Start Date'),
        validators=[MaxValueValidator(timezone.now)],
    )
    end_date = models.DateField(
        _('End Date'),
        validators=[MaxValueValidator(timezone.now)],
        default=timezone.now,
    )

    def __str__(self):
        def get_item_label(item):
            try:
                return item.name
            except AttributeError:
                return item.title

        label = (
            self.job.first().title
            if self.job.exists()
            else ''
            + ' - '
            + f'({self.start_date} - {self.end_date}) '
            + ', '.join(get_item_label(item) for item in self.stack.all() if item)
        )
        return label.strip()

    def clean(self):
        # start_date não pode ser no futuro
        if self.start_date and self.start_date > timezone.now().date():
            raise ValidationError({'start_date': _('A data de início não pode ser no futuro.')})

        # end_date não pode ser anterior à start_date
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError({
                'end_date': _('A data de término não pode ser anterior à data de início.')
            })

        # end_date não pode ser no futuro
        if self.end_date and self.end_date > timezone.now().date():
            raise ValidationError({'end_date': _('A data de término não pode ser no futuro.')})

    class Meta:
        verbose_name = _('Time Range')
        verbose_name_plural = _('Time Ranges')
        unique_together = ('start_date', 'end_date')
