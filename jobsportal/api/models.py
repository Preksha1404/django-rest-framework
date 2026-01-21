from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('recruiter', 'Recruiter'),
        ('candidate', 'Candidate'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Company(models.Model):
    name = models.CharField(max_length=500)
    recruiter =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='recruiters')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    

class Application(models.Model):
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(
        max_length=20,
        choices=[('applied','Applied'), ('shortlisted','Shortlisted')]
    )
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidates')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)