from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Job(models.Model):
	layer = models.IntegerField()
	slug = models.CharField(max_length=200)
	material = models.CharField(max_length=200)
	current_layer = models.IntegerField()
	machine_type = models.CharField(max_length=50)
	machine_index = models.CharField(max_length=50)
	completion_percentage = models.IntegerField()
	job_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.job_name
