from django.contrib import admin
from letswatch.models import UserProfile, VideoPost, Comment

# Register your models here.
# class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

# customised interface
admin.site.register(UserProfile)
admin.site.register(VideoPost)
admin.site.register(Comment)
