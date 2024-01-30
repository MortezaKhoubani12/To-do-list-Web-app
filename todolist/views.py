from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import *


class ListListView(ListView):
    model = ToDoList
    template_name = "todolist/index.html"

    def get_queryset(self):
        return ToDoList.objects.filter(user_list__user__id=self.request.user.id)


class TaskListView(ListView):
    model = ToDoTask
    template_name = "todolist/todo_list.html"

    def get_queryset(self):
        return ToDoTask.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = ToDoList
    form_class = ToDoListForm

    def form_valid(self, form):
        form.instance.user_list = self.request.user.userprofile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context


class TaskCreate(CreateView):
    model = ToDoTask
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        "completed",
        "starred",
        "priority_level",
        "created_date",
    ]

    def get_initial(self):
        initial_data = super(TaskCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(TaskCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new task"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class TaskUpdate(UpdateView):
    model = ToDoTask
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        "completed",
        "starred",
        "priority_level",
        # "created_date",
    ]

    def get_context_data(self):
        context = super(TaskUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit task"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])
