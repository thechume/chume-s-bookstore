from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^todays_deals$', views.todays_deals, name='todays_deals'),
	url(r'^cateogries$', views.todays_deals, name='categories'),
	url(r'^genres$', views.todays_deals, name='genres'),
]
