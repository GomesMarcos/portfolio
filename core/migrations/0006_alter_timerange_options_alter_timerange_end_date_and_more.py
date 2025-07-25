# Generated by Django 5.0.2 on 2025-07-25 14:35

import core.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_timerange_end_date_alter_timerange_start_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timerange',
            options={'ordering': ('-end_date',), 'verbose_name': 'Time Range', 'verbose_name_plural': 'Time Ranges'},
        ),
        migrations.AlterField(
            model_name='timerange',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, validators=[core.models.max_today], verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='timerange',
            name='start_date',
            field=models.DateField(validators=[core.models.max_today], verbose_name='Start Date'),
        ),
    ]
