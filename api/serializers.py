from rest_framework import serializers
from .models import Task

# import Task = MeetUp


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'


# class MeetSerializer(serializers.ModelSerializer):
    # class Meta:
    # model = MeetUp
    # fields ='__all__'