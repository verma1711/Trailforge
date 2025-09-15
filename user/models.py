from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class usermodel(models.Model):
    featured_image = models.ImageField(default='noprofile.webp')
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    user_mail = models.EmailField(max_length=200)
    user_created = models.DateTimeField(auto_now_add=True, null=True)
    user_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.username
    
@receiver(post_save, sender=User)
def autouser(sender, instance, created, **kwargs):
    if created:
        usermodel.objects.create(
        username = instance.username,
        user_mail = instance.email,
        ) 
    else:
        usermodel.username = instance.username,
        usermodel.user_mail = instance.email,
