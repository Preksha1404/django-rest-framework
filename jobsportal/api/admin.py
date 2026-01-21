from django.contrib import admin
from .models import Company, Job, Application

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','name','recruiter']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['id','title','description', 'skills', 'company']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=['id','candidate','job','status']