from django.conf.urls import url
from rango import views
#app_name ='rango'
#this is all under /rango/
urlpatterns=[
	url(r'^about/',views.about, name='about'),
	url(r'^add_category/$',views.add_category,name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$',views.user_login,name='login'),
	url(r'^signin/$',views.user_signin,name='signin'),
	url(r'^user/$',views.show_user,name='userprofile'),
	url(r'^signup/$',views.user_signup,name='signup'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^restricted/$',views.restricted,name='restricted'),
	url(r'^posts/$',views.post_list, name='post_list'),
	url(r'^$',views.index,name='index'),

]