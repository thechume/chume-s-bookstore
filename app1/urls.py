from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^search$', views.search, name="search"),
	url(r'^test', views.test, name="test"),
	url(r'^$', views.index, name='login'),
	url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^new_releases', views.new_releases, name='new_releases'),
	url(r'^todays_deals$', views.todays_deals, name='todays_deals'),
	url(r'^discover$', views.discover, name='discover'),
	url(r'^about$', views.about, name='about'),
	url(r'^contact$', views.contact, name='contact'),
	url(r'^genres$', views.genres, name='genres'),
	url(r'^categories$', views.categories, name='categories'),
	#books
	url(r'^warcross$', views.warcross, name='warcross'),
	#categories
	url(r'^categories/youngadult$', views.youngadult, name='youngadult'),
	url(r'^categories/adult$', views.adult, name='adult'),
	url(r'^categories/newadult$', views.newadult, name='newadult'),
	url(r'^categories/kids$', views.kids, name='kids'),
	#genres
	url(r'^genres/contemporary$', views.contemporary, name='contemporary'),
	url(r'^genres/comics$', views.comics, name='comics'),
	url(r'^genres/fantasy$', views.fantasy, name='fantasy'),
	url(r'^genres/thriller$', views.thriller, name='thriller'),
	url(r'^genres/mysteryandcrime$', views.mysteryandcrime, name='mysteryandcrime'),
	url(r'^genres/dystopia$', views.dystopia, name='dystopia'),
	url(r'^genres/nonfiction$', views.nonfiction, name='nonfiction'),
	url(r'^genres/romance$', views.romance, name='romance'),
	url(r'^genres/poetry$', views.poetry, name='poetry'),
	url(r'^genres/humour$', views.humour, name='humour'),
	url(r'^genres/horror$', views.horror, name='horror'),
	url(r'^genres/chicklit$', views.chicklit, name='chicklit'),
	url(r'^genres/sciencefiction$', views.sciencefiction, name='sciencefiction'),
	url(r'^genres/textbooks$', views.textbooks, name='textbooks'),
]
