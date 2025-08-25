from django.db import models

# Create your models here.
class usermodel(models.Model):
    featured_image = models.ImageField(default='noprofile.webp')
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    user_mail = models.EmailField(max_length=200)
    user_created = models.DateTimeField(auto_now_add=True, null=True)
    user_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user_name