from django.test import TestCase
from model_bakery import baker

from jobs.models import Job, Stack


class StackTestCase(TestCase):
    def test_create_task(self):
        python = baker.make(Stack, name='Python', is_current_stack=True)
        self.assertTrue(python.is_current_stack)
