from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime, date, timezone, time
from django.utils import timezone

class Genre(models.Model):

    max_length = 128
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

class Movie(models.Model):

    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='movies2/', blank=False)
    thumb=models.ImageField(upload_to='movies2/',blank=False)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=False, default='profile_images/default.png')

	def __str__(self):
		return self.user.username

class VideoPost(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):

    VideoPost = models.ForeignKey('letswatch.VideoPost', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Hotel(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/') 