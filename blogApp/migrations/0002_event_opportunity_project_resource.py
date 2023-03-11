# Generated by Django 3.1.7 on 2023-03-09 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('category', models.CharField(choices=[('Resume', 'Resume'), ('CV', 'CV'), ('Cover Letter', 'Cover Letter'), ('Masters', 'Masters'), ('PhD', 'PhD')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
                'db_table': 'resources',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('collaborators', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='project_photos')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Research', 'Research'), ('Independent Study', 'Independent Study'), ('SIP', 'SIP'), ('Honors Thesis', 'Honors Thesis')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('link', models.URLField()),
                ('opportunity_type', models.CharField(choices=[('Job', 'Job'), ('Internship', 'Internship'), ('Volunteer', 'Volunteer'), ('Research', 'Research'), ('Other', 'Other')], max_length=20)),
                ('paid', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'opportunity',
                'verbose_name_plural': 'opportunities',
                'db_table': 'opportunities',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('advisor', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('Hackathon', 'Hackathon'), ('Tech Talk', 'Tech Talk'), ('Research', 'Research'), ('Class', 'Class'), ('Workshop', 'Workshop')], max_length=20)),
                ('organizer', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('link', models.URLField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='event_photos')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'db_table': 'events',
            },
        ),
    ]
