from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttling import DemoUserRateThrottle

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,DemoUserRateThrottle]