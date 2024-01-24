from django.shortcuts import render
# todolistwebapp/todolist/views.py
from django.views.generic import ListView, TemplateView
from .models import *


# class HomePage(TemplateView):
#     def get(self, request, **kwargs):
#         list_data = []
#         all_list = ToDoList.objects.all()[:3]
#         for list in all_list:
#             list_data.append({
#                 'title': list.title,
#                 'cover': list.cover
#             })
#         context = {'list_data': list_data}
#         return render(request, 'home.html', context)


class ListListView(ListView):
    model = ToDoList
    template_name = "todolist/index.html"


class TaskListView(ListView):
    model = ToDoTask
    template_name = "todolist/todo_list.html"

    def get_queryset(self):
        return ToDoTask.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
