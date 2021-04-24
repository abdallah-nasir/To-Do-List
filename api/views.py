from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

# @api_view(['GET'])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/task-list/',
# 		'Detail View':'/task-detail/<str:pk>/',
# 		'Create':'/task-create/',
# 		'Update':'/task-update/<str:pk>/',
# 		'Delete':'/task-delete/<str:pk>/',
# 		}

# 	return Response(api_urls)

# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)


# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, id):
	task = Task.objects.get(id=id)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	task.delete()

# 	return Response('Item succsesfully delete!')



from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView,
	ListCreateAPIView

)
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class taskList(ListCreateAPIView):
	serializer_class=TaskSerializer
	def get_queryset(self):
		qs=Task.objects.filter(user=self.request.user).order_by('-id')
		return qs

class taskDetail(RetrieveAPIView):
	queryset=Task.objects.all()
	lookup_field="id"
	serializer_class=TaskSerializer
	permission_classes=[IsOwnerOrReadOnly]


class taskCreate(CreateAPIView):
	queryset=Task.objects.all()
	serializer_class=TaskSerializer
	# permission_classes=[IsAuthenticated]

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)

# class taskUpdate(RetrieveUpdateAPIView):
# 	lookup_field="id"
# 	serializer_class=TaskSerializer

class taskDelete(DestroyAPIView):
	queryset=Task.objects.all()
	lookup_field="id"
	serializer_class=TaskSerializer
	permission_classes=[IsOwnerOrReadOnly]
