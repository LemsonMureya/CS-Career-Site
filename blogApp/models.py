from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, **extra_fields)  # set is_active to True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    MAJOR_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Other', 'Other'),
    ]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Alumni', 'Alumni'),
        ('Faculty', 'Faculty'),
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('Other', 'Other'),
    ]
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    major_minor = models.CharField(max_length=255, choices=MAJOR_CHOICES, default='Computer Science')
    position = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    class_year = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='Student') 
    photo = models.ImageField(upload_to='user_photos/', blank=True, default='user_photos/default-avatar.png')
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #linked,twitter,fb etc, portfolio

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.last_name

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Opportunity(models.Model):
    JOB = 'Job'
    INTERNSHIP = 'Internship'
    VOLUNTEER = 'Volunteer'
    RESEARCH = 'Research'
    OTHER = 'Other'
    TYPE_CHOICES = [
        (JOB, 'Job'),
        (INTERNSHIP, 'Internship'),
        (VOLUNTEER, 'Volunteer'),
        (RESEARCH, 'Research'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    link = models.URLField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    opportunity_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    location = models.CharField(max_length=255)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    is_open = models.BooleanField(default=True)
    is_remote = models.BooleanField(default=False)  # Remote or on-site
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Ensure the slug is unique
            original_slug = slugify(self.title)
            queryset = Opportunity.objects.all().exclude(pk=self.pk)
            unique_slug = original_slug
            num = 1
            while queryset.filter(slug=unique_slug).exists():
                unique_slug = f'{original_slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(Opportunity, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'opportunities'
        verbose_name = 'opportunity'
        verbose_name_plural = 'opportunities'

class Event(models.Model): #make optional values
    HACKATHON = 'Hackathon'
    TECH_TALK = 'Tech Talk'
    RESEARCH = 'Research'
    CLASS = 'Class'
    WORKSHOP = 'Workshop'
    OTHER = 'Other'
    TYPE_CHOICES = [
        (HACKATHON, 'Hackathon'),
        (TECH_TALK, 'Tech Talk'),
        (RESEARCH, 'Research'),
        (CLASS, 'Class'),
        (WORKSHOP, 'Workshop'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    organizer = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    # start_time =  models.DateTimeField(null=False, blank=False) #remove these
    # end_time = models.DateTimeField(null=False, blank=False)
    link = models.URLField() #make it optional
    photo = models.ImageField(upload_to='event_photos', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate a slug if it does not exist
        if not self.slug:
            # Create a base slug from the title
            base_slug = slugify(self.title)
            # Append a random string to ensure uniqueness
            unique_slug = base_slug + "-" + get_random_string(5)
            self.slug = unique_slug
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'

class Resource(models.Model):# main blog post
    RESUME = 'Resume'
    CV = 'CV'
    COVER_LETTER = 'Cover Letter'
    MASTERS = 'Masters'
    PHD = 'PhD'
    OTHER = 'Other'
    CATEGORY_CHOICES = [
        (RESUME, 'Resume'),
        (CV, 'CV'),
        (COVER_LETTER, 'Cover Letter'),
        (MASTERS, 'Masters'),
        (PHD, 'PhD'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'resources'
        verbose_name = 'resource'
        verbose_name_plural = 'resources'


class Project(models.Model):
    RESEARCH = 'Research'
    INDEPENDENT_STUDY = 'Independent Study'
    SIP = 'SIP'
    HONORS_THESIS = 'Honors Thesis'
    OTHER = 'Other'
    CATEGORY_CHOICES = [
        (RESEARCH, 'Research'),
        (INDEPENDENT_STUDY, 'Independent Study'),
        (SIP, 'SIP'),
        (HONORS_THESIS, 'Honors Thesis'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    collaborators = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='project_photos', blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'projects'
        verbose_name = 'project'
        verbose_name_plural = 'projects'

class BlogPost(models.Model):
    INTERVIEW_PREP = 'Interview Prep'
    TECHNICAL_INTERVIEWS = 'Technical Interviews'
    BEHAVIORAL_INTERVIEWS = 'Behavioral Interviews'
    GRAD_SCHOOL_PREP = 'Grad School Prep'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (INTERVIEW_PREP, 'Interview Prep'),
        (TECHNICAL_INTERVIEWS, 'Technical Interviews'),
        (BEHAVIORAL_INTERVIEWS, 'Behavioral Interviews'),
        (GRAD_SCHOOL_PREP, 'Grad School Prep'),
        (OTHER, 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default=OTHER)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)  # Requires admin approval
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    # views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
