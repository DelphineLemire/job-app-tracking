from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created}"


class Source(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class JobSource(models.Model):
    TYPES_CHOICES = [
        ("CDI", "CDI"),
        ("CDD", "CDD"),
        ("INT", "INTERIM"),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    ref_source = models.CharField(max_length=25, null=True, blank=True)
    ref_company = models.CharField(max_length=25, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    full_remote = models.BooleanField(null=True, blank=True)
    finale_company = models.BooleanField(null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=25, choices=TYPES_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.source}/{self.job}"
