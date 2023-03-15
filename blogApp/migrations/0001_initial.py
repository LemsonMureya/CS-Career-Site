# Generated by Django 3.1.7 on 2023-03-11 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True)),
                ('major_minor', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Other', 'Other')], default='Computer Science', max_length=255)),
                ('position', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('class_year', models.PositiveIntegerField(blank=True, null=True)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Alumni', 'Alumni'), ('Faculty', 'Faculty'), ('Admin', 'Admin'), ('Staff', 'Staff'), ('Other', 'Other')], default='Student', max_length=255)),
                ('photo', models.ImageField(blank=True, default='default-avatar.png', upload_to='user_photos/')),
                ('verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('category', models.CharField(choices=[('Resume', 'Resume'), ('CV', 'CV'), ('Cover Letter', 'Cover Letter'), ('Masters', 'Masters'), ('PhD', 'PhD'), ('Other', 'Other')], max_length=20)),
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
                ('category', models.CharField(choices=[('Research', 'Research'), ('Independent Study', 'Independent Study'), ('SIP', 'SIP'), ('Honors Thesis', 'Honors Thesis'), ('Other', 'Other')], max_length=20)),
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
                ('event_type', models.CharField(choices=[('Hackathon', 'Hackathon'), ('Tech Talk', 'Tech Talk'), ('Research', 'Research'), ('Class', 'Class'), ('Workshop', 'Workshop'), ('Other', 'Other')], max_length=20)),
                ('organizer', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('link', models.URLField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='event_photos')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'db_table': 'events',
            },
        ),
    ]