# management/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project, Task

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_admin', 'is_team_lead', 'is_team_member']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'assigned_to']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'project', 'assigned_to']