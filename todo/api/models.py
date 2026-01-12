from django.db import models

# Create your models here.
class Task(models.Model):
    class TaskEnum(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'

    title = models.CharField(max_length=500)
    status = models.CharField(
        max_length=20,
        choices=TaskEnum.choices,
        default=TaskEnum.PENDING
    )
    duration = models.DurationField()
