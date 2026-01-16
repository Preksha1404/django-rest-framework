from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission
from api.customauth import CustomAuthentication

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes=[BasicAuthentication]
    # authentication_classes=[SessionAuthentication]
    # authentication_classes=[TokenAuthentication]
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[MyPermission]

# class StudentReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer