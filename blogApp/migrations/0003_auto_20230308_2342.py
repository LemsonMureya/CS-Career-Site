# Generated by Django 3.1.7 on 2023-03-09 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_event_opportunity_project_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='advisor',
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='default-avatar.png', upload_to='user_photos/'),
        ),
    ]
