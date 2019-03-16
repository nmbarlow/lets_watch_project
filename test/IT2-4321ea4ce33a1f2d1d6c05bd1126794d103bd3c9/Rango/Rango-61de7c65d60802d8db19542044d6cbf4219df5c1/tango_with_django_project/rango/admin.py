from django.contrib import admin

from rango.models import Category, Page
from rango.models import UserProfile

# Register your models here.



class PageAdmin(admin.ModelAdmin):
	#note, this is not a method !!!
	list_display=("title","category","url")

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

#custom view
admin.site.register(Category,CategoryAdmin)
#show default 
#admin.site.register(Category)

admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)