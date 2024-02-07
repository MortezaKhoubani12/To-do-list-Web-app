from django.forms import ModelForm
from .models import ToDoList


# define a form for the to-do list model
class ToDoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'cover']
