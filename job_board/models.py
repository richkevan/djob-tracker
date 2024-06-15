from django.db import models

# Create your models here.
class Job(models.Model):
  pk = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  description = models.TextField()
  location = models.CharField(max_length=100)
  min_salary = models.IntegerField()
  max_salary = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  status  = models.ManyToManyField("Status", blank=False, related_name="job status")
  updated_at = models.DateTimeField(auto_now=True)
  
class Status(models.Model):
  pk = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)