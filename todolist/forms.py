from django import forms
from .models import ToDoList


# define a form for the to-do list model
class ToDoListForm(forms.ModelForm):
    # define the fields of the form
    class Meta:
        model = ToDoList  # tell the form which model to use
        fields = ['title', 'cover']  # tell the form which fields to use
