from django.contrib.auth.models import User
from todolist.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


# Define a receiver function for the post_save signal
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        avatar = instance.avatar
        UserProfile.objects.create(user=instance, avatar=avatar)
