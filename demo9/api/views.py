from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

# Filtering based on passby field
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     # queryset=Student.objects.filter(passby='user1')
#     serializer_class=StudentSerializer

#     # Only current user data will be showed to that current user
#     # def get_queryset(self):
#     #     user=self.request.user
#     #     return Student.objects.filter(passby=user)

#     filter_backends=[DjangoFilterBackend]
#     filterset_fields = ['city']

# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#     filter_backends=[SearchFilter]
#     # search_fields = ['name','city']
#     search_fields = ['^name']

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    filter_backends=[OrderingFilter]
    ordering_fields=['name']