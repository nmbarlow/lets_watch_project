from django.conf.urls import url
from letswatch import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_genre/$', views.add_genre, name='add_genre'),
    url(r'^genre/(?P<genre_name_slug>[\w\-]+)/add_movie/$', views.add_movie, name='add_movie'),
    url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$',
        views.show_genre, name='show_genre'),
    url(r'^register/$',
        views.register,
        name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/(?P<username>[\w\-]+)/$',views.profile, name='profile'),


]
