# Generated by Django 4.1.9 on 2023-06-13 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_source', models.CharField(blank=True, max_length=25, null=True)),
                ('ref_company', models.CharField(blank=True, max_length=25, null=True)),
                ('place', models.CharField(blank=True, max_length=50, null=True)),
                ('full_remote', models.BooleanField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.CharField(blank=True, choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('INT', 'INTERIM')], max_length=25, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.source')),
            ],
        ),
    ]