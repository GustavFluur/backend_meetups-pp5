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


# CRUD Operation using Django REST API and React JS 2022

# PART 3

#from rest_framework import serializers
#from api.models import Patient

# class PatientSerializer(serializers.HyperlinkedModelSerializer):
        #class Meta:
        #model = Patient
        #fields = ['patient_id', 'first_name', 'last_name', 'blood']

