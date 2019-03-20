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
    time_stamp = models.DateTimeField(auto_now_add=True) #will automatically populate this with current time
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=200)
    year = models.CharField(max_length=4,blank=True)
    description = models.CharField(max_length=600)
    views = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='movies2/', blank=False)
    thumb = models.ImageField(upload_to='movies2/',blank=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class WatchList(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    time_stamp = models.DateTimeField(auto_now_add=True) #will automatically populate this with current time
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'movie')


    def __str__(self):
        return self.user.user.username + ": " + self.movie.title

class MovieViews(models.Model):
    movie = models.ForeignKey(Movie)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'time_stamp')

    def __str__(self):
        return self.movie.title + ": views"

class UserProfile(models.Model):

	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images/', blank=True)
    #add default if it works
	def __str__(self):
		return self.user.username

class VideoPost(models.Model):

    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Review(models.Model):#(comments)

    date = models.DateField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    content = models.TextField(blank=True)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        # user and the movie as primary key
        unique_together = ('user', 'movie',)

    def __str__(self):
        return self.user.user.username + ": " + self.movie.title

    def __unicode__(self):
        return self.user.user.username + ": " + self.movie.name

class Hotel(models.Model):

    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
