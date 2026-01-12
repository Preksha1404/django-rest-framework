"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

# router.register('task',views.TaskViewSet,basename='task')
router.register('task',views.TaskModelViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('task/', views.TaskAPI.as_view()),
    # path('task/<int:id>', views.TaskAPI.as_view()),
    # path('task/', views.LCTaskAPI.as_view()),
    # path('task/<int:pk>', views.RUDTaskAPI.as_view()),
    # path('task/',views.TaskListCreate.as_view()),
    # path('task/<int:pk>',views.TaskRetrieveUpdateDestroy.as_view()),
    path('',include(router.urls))
]
