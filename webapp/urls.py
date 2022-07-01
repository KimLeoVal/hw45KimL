from django.urls import path

from hw45KimL.webapp.views import index_view, create_task, tasks_view, task_view, update_task, delete_task

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create/', create_task, name='create_task'),
    path('tasks/', tasks_view, name='tasks_view'),
    path('task/<pk>', task_view, name='task_view'),
    path('task/<pk>/update', update_task, name='update_task'),
    path('task/<pk>/delete', delete_task, name='delete_task'),


]
