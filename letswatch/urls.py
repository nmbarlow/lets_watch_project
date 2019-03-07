from django.conf.urls import url
from letswatch import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$',
        views.register,
        name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^videos/$', views.videos, name='videos'),

]
