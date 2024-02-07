from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


def validate_image(file):
    image_format = file.name.split('.')[-1].lower()
    if image_format not in ['jpg', 'png']:
        raise ValidationError('Unsupported file format. Only jpg and png media are allowed !')
    image_size = file.size
    if image_size > 500 * 1024:
        raise ValidationError('File size is too large.Maximum size is 500 KB !')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(
        upload_to='user_avatar/',
        default='user_avatar/avatar.jpg',
        validators=[validate_image],
        null=True,
        blank=True)

    def __str__(self):
        # return self.user.username
        return self.user.get_full_name()


class ToDoList(models.Model):
    user_list = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    cover = models.FileField(upload_to='list_cover/',
                             default='list_cover/default.png',
                             validators=[validate_image],
                             null=True,
                             blank=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoTask(models.Model):
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, blank=False)
    due_date = models.DateTimeField(default=one_week_hence)
    completed = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)
    PRIORITY_CHOICES = [('low', 'Low'), ('normal', 'Normal'), ('high', 'High')]
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='normal')

    def get_absolute_url(self):
        return reverse("task-update", args=[str(self.todo_list.id), str(self.id)])

    # def __str__(self):
    #     return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]

