# Generated by Django 4.1.9 on 2023-06-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_created_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsource',
            name='finale_company',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]