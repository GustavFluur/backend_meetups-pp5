from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

# import TaskSerializer => MeetSerializer
# import Task => MeetUp

# CRUD Operation using Django REST API and React JS 2022
# PART 4

#from rest_framework import viewsets
# from api.serializers import PatientSerializer


#class PatientViewSet(viewsets.ModelViewSet):
    #"""
    #A viewset for viewing and editing user instances.
    #"""
    #serializer_class = UserSerializer
    #queryset = User.objects.all()

# class PatientViewSet(viewsets.ModelViewSet)
	# queryset = Patient.objects.all()

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

# Task = MeetUp

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	# meets = MeetUp.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	# serializer = MeetSerializer(meets, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	# meets = MeetUp.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	# serializer = MeetSerializer(meets, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	# serializer = MeetSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	# meet = MeetUp.object.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	# meet = MeetUp.object.get(id=pk)
	task.delete()
	# meet.delete()

	return Response('Item succsesfully delete!')

	# return Response('Activity has successfully been deleted!')
