from django import forms
from .models import ToDoList


# define a form for the to-do list model
class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'cover']
