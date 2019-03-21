from django.conf.urls import url
from letswatch import views
from django.views.generic.base import TemplateView
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_genre/$', views.add_genre, name='add_genre'),
    url(r'^genre/(?P<genre_name_slug>[\w\-]+)/add_movie/$', views.add_movie, name='add_movie'),
    url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$', views.show_genre, name='show_genre'),
    url(r'^movies/(?P<movie_title_slug>[\w\-]+)/$', views.show_movie, name='show_movie'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^movies/(?P<movie_title_slug>[\w\-]+)/list_reviews/$', views.list_reviews, name='list_reviews'),
    
    url(r'^image_upload/$', views.hotel_image_view, name='image_upload'),
    url(r'^success/$', views.success, name='success'),
    #url(r'^register_profile/$', views.register_profile, name='register_profile'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/(?P<username>[\w\-]+)/$',views.profile, name='profile'),

    url(r'^movies/(?P<movie_title_slug>[\w\-]+)/ajax_reviews/$', views.ajax_reviews, name='ajax_reviews'),
   

]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()