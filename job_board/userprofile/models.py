from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from job.models import Application

class Userprofile(models.Model):
  user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
  is_employer = models.BooleanField(default=False)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
  application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='conversationmessages')
  content = models.TextField()
  created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add = True)

  class Meta:
    ordering = ['created_at']