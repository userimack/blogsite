from django.conf.urls import url
from blogapp import views

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$',views.login,name='login'),
	url(r'^success/$',views.success,name='success'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^profile_view/$',views.profile_view,name='profile_view'),
]