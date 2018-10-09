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
