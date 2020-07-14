from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os
from django.dispatch import receiver
from django.db.models.signals import post_save

#from private_storage.fields import PrivateFileField



class Post(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(null=True,blank=True,upload_to='Files')#PrivateFileField("File",null=True)
	content = models.TextField()
	manager = models.ManyToManyField("UserProfile")
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

# class contactsManager(models.Manager):
# 	def get_query_set(self):
# 		return 

class Contacts(models.Model):
	posts = models.ForeignKey('Post',on_delete=models.CASCADE,null=True)
	contact = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

class UserProfile(models.Model):
    ENDUSER = 1
    MANAGER = 2
    ROLE_CHOICES = (('Manager', 'manager'), ('EndUser', 'EndUser'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, null=True, blank=True,max_length=100)
    contact = models.ManyToManyField('self')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
