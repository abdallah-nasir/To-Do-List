from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
  user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  @property
  def owner(self):
    return self.user
  def __str__(self):
    return self.title