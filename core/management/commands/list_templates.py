from pathlib import Path

from django import template as django_template
from django.core.management.base import BaseCommand, no_translations


class Command(BaseCommand):
    help = 'Show all Django Templates'

    @no_translations
    def handle(self, *args, **options):
        """
        Retrieves a list of all template file paths detected by Django's template loaders.
        Excludes templates located within site-packages directories.
        """
        template_directories = []
        for engine in django_template.loader.engines.all():
            # Exclude site-packages directories to filter out installed app templates
            template_directories.extend(
                x for x in engine.template_dirs if 'site-packages' not in str(x)
            )

        template_files = []
        for directory in template_directories:
            # Recursively find all .html files within the template directories
            template_files.extend(x for x in Path(directory).glob('**/*.html') if x.is_file())

        self.stdout.write('\n'.join(str(template) for template in template_files))
