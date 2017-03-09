from django.contrib import admin
from .models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
	list_display = ('job_name', 'slug', 'material', 'layer', 'machine_index')	

admin.site.register(Job, JobAdmin)
