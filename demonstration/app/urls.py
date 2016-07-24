# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^test/$',views.test,name='test'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^history/$',views.history,name='history'),
	url(r'^about/$',views.about,name='about')


]
