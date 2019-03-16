from django.conf.urls import url
from django.contrib import admin
from letswatch import views
from .views import (search)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^register/$',
        views.register,
        name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^profile/$',views.profile, name='profile'),
    url(r'^search/$', views.search, name='search'),

]
