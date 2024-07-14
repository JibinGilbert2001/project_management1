from django.urls import path
from .views import register, user_login, user_logout, home
from .views import create_project, edit_project, delete_project, project_list
from .views import task_list, edit_task, create_task, delete_task


urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('projects/', project_list, name='project_list'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/edit/<int:project_id>/', edit_project, name='edit_project'),
    path('projects/delete/<int:project_id>/', delete_project, name='delete_project'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]
