from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
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
	category=models.ForeignKey(Category)
	title=models.CharField(max_length=128)
	url=models.URLField()
	views=models.IntegerField(default=0)

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user =models.OneToOneField(User)
	description=models.CharField(max_length=100,blank=True,default="")
	image =models.ImageField(upload_to="profile_image",blank=True)

	def __str__(self):
		return self.user.username
