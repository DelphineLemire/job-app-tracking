from django.db import models

from jobs.models import Job


# Create your models here.
class Candidacy(models.Model):
    STATUS_CHOICES = [
        ("DRAFT", "draft"),
        ("SEND", "send"),
        ("CALL", "first call"),
        ("REJECTED", "rejected"),
        ("VALIDATED", "validated"),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    last_event = models.DateField()

    class Meta:
        verbose_name_plural = "candidacies"
