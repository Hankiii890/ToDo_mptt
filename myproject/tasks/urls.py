from django.urls import path
from . import views

urlpatterns = [
    path('', views.lst_tasks, name='list_task'),
    path('create/', views.task_created, name='create_task'),
    path('edit/<int:task_id>', views.task_edite, name='task_edite'),
]


