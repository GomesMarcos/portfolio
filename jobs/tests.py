from django.test import TestCase
from model_bakery import baker

from jobs.models import Job, Stack


class StackTestCase(TestCase):
    def test_create_task(self):
        python = baker.make(Stack, name='Python', is_current_stack=True)
        self.assertTrue(python.is_current_stack)

    def test_get_time_worked(self):
        stack = baker.make(Stack, name='Python', is_current_stack=True)
        time_range1 = baker.make('core.TimeRange', start_date='2022-01-01', end_date='2022-06-01')
        time_range2 = baker.make('core.TimeRange', start_date='2022-07-01', end_date='2025-12-01')
        time_range3 = baker.make('core.TimeRange', start_date='2024-07-01', end_date='2025-12-01')
        stack.time_range.add(time_range1, time_range2, time_range3)

        expected_time_worked = {'years': 5, 'months': 3}
        self.assertEqual(stack.get_time_worked, expected_time_worked)
