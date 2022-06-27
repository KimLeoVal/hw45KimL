from django.urls import path



from hw45KimL.webapp.views import task_view,index_view, create_task, tasks_view

urlpatterns = [
    path('', index_view),
    path('create/', create_task),
    path('tasks/', tasks_view),
    path('tasks/task/<pk>', task_view),


]