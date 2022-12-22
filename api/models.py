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


# CRUD Operation using Django REST API and React JS 2022
# PART 1
#class Patient(models.Model):
  #patient_id = models.BigAutoField(primary_key=True)
  #first_name = models.CharField(max_length=50)
  #last_name = models.CharField(max_length=50)
  #blood = models.CharField(max_length=50)

  #def __str__(self):
  #  return self.first_name
