from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']


admin.site.register(UserProfile, UserProfileAdmin)


class ToDoListAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'cover']


admin.site.register(ToDoList, ToDoListAdmin)


class ToDoTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'list_title', 'completed', 'starred', 'priority_level']
    list_filter = ['starred', 'completed', 'priority_level']

    def list_title(self, obj):
        return obj.todo_list.title


admin.site.register(ToDoTask, ToDoTaskAdmin)
