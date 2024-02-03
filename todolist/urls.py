from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListListView.as_view(),
         name="index"),
    path("list/<int:list_id>/", views.TaskListView.as_view(),
         name="list"),

    # CRUD patterns for ToDo Lists
    path("list/add/", views.ListCreate.as_view(),
         name="list-add"),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(),
         name="list-delete"),

    # CURD patterns for ToDo Tasks
    path("list/<int:list_id>/task/add/", views.TaskCreate.as_view(),
         name="task-add"),
    path("list/<int:list_id>/task/<int:pk>/", views.TaskUpdate.as_view(),
         name="task-update"),
    path("list/<int:list_id>/task/<int:pk>/delete/", views.TaskDelete.as_view(),
         name="task-delete"),
]
