from django.db import models


# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

# Task => MeetUp 
# title = models.CharField(max_length=200)
# first_name = models.CharField(max_lenght=100)
# occupation = models.CharField(max_length=100, blank=True, default='') 
# city = models.CharField(_('Where?'), max_length = 100, blank = True)
# field_name = models.TextField(_('Activity'))