from django_filters import FilterSet, ChoiceFilter, OrderingFilter
from .models import *

STARRED_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),)
COMPLETED_CHOICES = (
    (True, 'Done ✔'),
    (False, 'Doing □'),)
PRIORITY_CHOICES = (
    ('low', 'Low'),
    ('normal', 'Normal'),
    ('high', 'High'),)
ORDER_BY_CHOICES = (
    ('due_date', 'Ascending'),
    ('-due_date', 'Descending'),)


class TaskFilter(FilterSet):
    starred = ChoiceFilter(choices=STARRED_CHOICES)
    completed = ChoiceFilter(choices=COMPLETED_CHOICES)
    priority_level = ChoiceFilter(choices=PRIORITY_CHOICES)
    due_date = OrderingFilter(choices=ORDER_BY_CHOICES)

    class Meta:
        model = ToDoTask
        fields = ["starred", "completed", "priority_level", "due_date"]
