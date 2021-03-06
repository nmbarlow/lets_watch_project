from django.contrib import admin
from letswatch.models import Genre, Movie, UserProfile, VideoPost, Review, WatchList

# Register your models here.
# class to customise the Admin Interface
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre','url', 'year')

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# customised interface
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(UserProfile)
admin.site.register(VideoPost)
admin.site.register(WatchList)

admin.site.register(Review,ReviewAdmin)
