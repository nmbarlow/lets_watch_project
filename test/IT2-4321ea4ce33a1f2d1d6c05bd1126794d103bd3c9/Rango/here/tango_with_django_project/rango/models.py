from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=128,unique=True)
	views=models.IntegerField(default=0)
	likes=models.IntegerField(default=0)
	slug=models.SlugField(unique=True)

	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		super(Category,self).save(*args,**kwargs)
	#fix the typo when viewing it in the admin page
	class Meta:
		verbose_name_plural='Categories'
	#equivalent to toString() method
	def __str__(self):
		return self.name


class Page(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	title=models.CharField(max_length=128)
	url=models.URLField()
	views=models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Movie(models.Model):
	
	title=models.CharField(max_length=128)
	trailer=models.URLField()
	genre= models.CharField()
	views=models.IntegerField(default=0)
	image=models.ImageField(upload_to="movie_thumb",blank=False)
	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user =models.OneToOneField(User,on_delete=models.CASCADE,)
	website=models.URLField(blank=True)
	picture =models.ImageField(upload_to='profile_images',blank=True)

	def __str__(self):
		return self.user.username


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

