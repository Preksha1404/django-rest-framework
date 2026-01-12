from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):
#         student = Student.objects.all()
#         serializer=StudentSerializer(student,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer=StudentSerializer(student)
#             return Response(serializer.data)
        
#     def create(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         id = pk
#         student = Student.objects.get(id=id)
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         id = pk
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response(status=status.HTTP_200_OK)

# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer