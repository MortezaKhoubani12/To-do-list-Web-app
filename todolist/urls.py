from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.TaskListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    # CURD patterns for ToDoTasks
    path("list/<int:list_id>/task/add/", views.TaskCreate.as_view(), name="task-add"),
    path("list/<int:list_id>/task/<int:pk>/", views.TaskUpdate.as_view(), name="task-update"),
]
