from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class job(models.Model):
  title = models.CharField(max_length=255)
  show_description = models.TextField()
  long_description = models.TextField(blank=True, null=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
  created_at = models.DateTimeField(auto_now_add=True)
  changed_at = models.DateTimeField(auto_now=True)
  