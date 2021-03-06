"""lets_watch_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from letswatch import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^letswatch/', include('letswatch.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # url(r'^settings/$', views.settings, name='settings'),
    # url(r'^settings/password/$', views.password, name='password'),
    url(r'^movie/(?P<movie_name_slug>[\w\-]+)/rate/$', views.rate_movie, name='rate_movie'),
    url(r'^movie/(?P<movie_name_slug>[\w\-]+)/review/$', views.add_review, name='add_review'),
    url(r'^watchlist/$', views.watchlist, name='watchlist'),
    url(r'^trending/$', views.trending, name='trending'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
