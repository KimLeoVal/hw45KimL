from django.urls import path

from webapp.views import index_view, create_task, tasks_view

urlpatterns = [
    path('', index_view),
    path('create/', create_task),
    path('tasks/', tasks_view)

]