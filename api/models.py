from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect,reverse

# Create your models here.

class Task(models.Model):
  user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def get_absolute_task(self):
    return redirect(reverse("api:task-detail", kwargs={"id":self.id}))

  def get_absolute_update(self):
    return redirect(reverse("api:task-update", kwargs={"id":self.id}))  

  def get_absolute_delete(self):
    return redirect(reverse("api:task-delete", kwargs={"id":self.id}))
  @property
  def owner(self):
    return self.user
  def __str__(self):
    return self.title