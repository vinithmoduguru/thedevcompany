from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


# @receiver(post_save, sender=Profile )
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcome to Dev Search'
        message = f"Hey {user.first_name},\n I’m Vinith, the owner of thedevcompany and I’d like to personally thank you for signing up to our website. We established thedevcompany in order to occassionally update your work and stay connected.\n\nI’d love to hear what you think of this website and if there is anything we can improve. If you have any questions, please reply to this email. I’m always happy to help!\n\nThanks and be well,\nVinith"


        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
