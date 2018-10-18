from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'mysite3/new_releases.html')
	
	
def todays_deals(request):
    return render(request,'mysite3/todays_deals.html')
	
def genres(request):
    return render(request,'mysite3/genres.html')

def categories(request):
    return render(request,'mysite3/categories.html')

def warcross(request):
    return render(request,'mysite3/books/warcross.html')
	
def youngadult(request):
    return render(request,'mysite3/category_s/youngadult.html')
	
def contemporary(request):
    return render(request,'mysite3/genre_s/contemporary.html')
	
def discover(request):
    return render(request,'mysite3/discover.html')
	
def about(request):
    return render(request,'mysite3/about.html')
	
def contact(request):
    return render(request,'mysite3/contact.html')