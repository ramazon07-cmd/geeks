from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return f"{self.email} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    course = models.ManyToManyField('Course', related_name="categories")

    def __str__(self):
        return self.name

# Create your models here.
class Course(models.Model):
    AVAILABILITY_CHOICES = [
        ('Beginner', 'beginner'),
        ('Intermediate', 'intermediate'),
        ('Advance', 'advance'),
    ]
    name = models.CharField(max_length=255)
    trailer = models.FileField(upload_to='trailers/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name="courses")
    image = models.ImageField(upload_to='courses/')
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_courses")
    status = models.CharField(max_length=100, choices=AVAILABILITY_CHOICES, default='active')
    total_videos = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)
    description = models.TextField()

    def formatted_duration(self):
        minutes, seconds = divmod(self.total_duration, 60)
        return f"{minutes}m {seconds}s"

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    progress = models.IntegerField(default=0)
    videos = models.ManyToManyField('Video', related_name='lessons')
    is_completed = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    file = models.FileField(upload_to='lessons/')
    duration = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def formatted_duration(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{minutes}m {seconds}s"

    def __str__(self):
        return self.title

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    first_name = models.CharField(max_length=30)
    courses = models.ManyToManyField('Course', related_name="teacher_category", blank=True)
    last_name = models.CharField(max_length=30)
    salary = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    courses = models.ManyToManyField('Course', related_name='teachers', blank=True)
    bio = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=25, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
