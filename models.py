from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_team_lead = models.BooleanField(default=False)
    is_team_member = models.BooleanField(default=False)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projects')

    def __str__(self):
        return self.title

class Task(models.Model):
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = [
        (TODO, 'To-Do'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')

    def __str__(self):
        return self.title
