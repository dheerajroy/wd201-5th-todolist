from unicodedata import name
from django.urls import path
from .views import Views

views = Views()
urlpatterns = [
    path('all_tasks/', views.all_tasks, name='all_tasks'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('complete_task/<int:index>/', views.complete_task, name='complete_task'),
    path('add-task/', views.add_task, name='add_task'),
    path('delete-task/<int:index>/', views.delete_task, name='delete_task'),
    path('tasks/', views.tasks, name='tasks')
]
