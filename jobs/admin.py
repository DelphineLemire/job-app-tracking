from django.contrib import admin

from jobs import models

# Register your models here.
admin.site.register(models.Source)
admin.site.register(models.Job)
admin.site.register(models.JobSource)
