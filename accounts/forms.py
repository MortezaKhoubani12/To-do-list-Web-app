from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.FileField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('avatar',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
        return user
