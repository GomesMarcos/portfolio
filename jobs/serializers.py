from rest_framework import serializers

from .models import Job, Stack, StackTimeRange


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['start_date', 'end_date', 'description', 'logo', 'stack', 'is_current_job']


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stack
        fields = ['name', 'is_current_stack', 'get_time_worked']


class StackTimeRangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StackTimeRange
        fields = '__all__'
