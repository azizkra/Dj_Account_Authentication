from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)# instance=> هاد النسخة الجديدة من اليوز الي رح ينشاْ

@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()