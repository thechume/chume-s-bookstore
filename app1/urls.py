from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='new_releases'),
	url(r'^todays_deals$', views.todays_deals, name='todays_deals'),
	url(r'^genres$', views.genres, name='genres'),
	url(r'^categories$', views.categories, name='categories'),
	url(r'^warcross$', views.warcross, name='warcross'),
	url(r'^categories/youngadult$', views.youngadult, name='youngadult'),
	url(r'^genres/contemporary$', views.contemporary, name='contemporary'),
	url(r'^discover$', views.discover, name='discover'),
	url(r'^about$', views.about, name='about'),
	url(r'^contact$', views.contact, name='contact'),
]
