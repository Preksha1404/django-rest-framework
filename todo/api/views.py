from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
# Create your views here.

# Using -> class-based rest api view
# class TaskAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             task = Task.objects.get(id=id)
#             serializer = TaskSerializer(task)
#             return Response(serializer.data)
#         task = Task.objects.all()
#         serializer = TaskSerializer(task,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         serializer=TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, pk, format=None):
#         id = pk
#         task = Task.objects.get(id=id)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, pk, format=None):
#         id = pk
#         task = Task.objects.get(id=id)
#         serializer = TaskSerializer(task, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format=None):
#         id = pk
#         task = Task.objects.get(id=id)
#         task.delete()
#         return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)


# Using GenericView and mixins
# class LCTaskAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class RUDTaskAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# Using APIView -> extends GenericAPIView and mixins
# class TaskListCreate(ListCreateAPIView):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer

# class TaskRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer


# Using ViewSet
# class TaskViewSet(viewsets.ViewSet):
#     def list(self,request):
#         task = Task.objects.all()
#         serializer=TaskSerializer(task,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             task = Task.objects.get(id=id)
#             serializer=TaskSerializer(task)
#             return Response(serializer.data)
        
#     def create(self,request):
#         serializer=TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         id = pk
#         task = Task.objects.get(id=id)
#         serializer=TaskSerializer(task,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         id = pk
#         task = Task.objects.get(id=id)
#         task.delete()
#         return Response(status=status.HTTP_200_OK)


# Using ModelViewSet
class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer