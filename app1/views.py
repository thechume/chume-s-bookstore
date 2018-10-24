from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Authors, Cart, Discount, Users
from django.db import connection
import mysql.connector as mariadb
from django.views import generic


# Create your views here.

def search(request):
    if request.method == 'POST':
        book_name =  request.POST.get('search')
        status = Books.objects.filter(title__icontains=book_name)
        if status==None :
            status = Authors.objects.filter(a_name__icontains=book_name)
        #status = Books.objects.raw('SELECT * FROM Books natural join Authors WHERE title LIKE "%Koi%"')
        return render(request,"mysite3/search.html",{'data':status})
    if request.method == 'GET':
        return render(request,'mysite3/new_releases.html',{})

def index(request):
    return render(request,'mysite3/login.html')
	
def test(request):
    if request.method == 'POST':
        book_name =  request.POST.get('search')
        status = Books.objects.filter(title__icontains=book_name)
        return render(request,'mysite3/search.html',{'data':status})
    if request.method == 'GET':
        book_name="Warcro"
        status = Books.objects.filter(title__icontains=book_name)
        return render(request,'mysite3/search.html',{'data':status})
	
def sign_up(request):
    return render(request,'mysite3/sign_up.html')
	
'''def test(request):
    mariadb_connection = mariadb.connect(user='root', password='password', database='bookrecs')
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT * FROM authors")
    row = []
    i = cursor.fetchone()
    row.append(i)
    while i is not None:
        i = cursor.fetchone()
        row.append(i)
    cursor.close()
    mariadb_connection.close()'''

def new_releases(request):
    return render(request,'mysite3/new_releases.html')
	
def todays_deals(request):
    return render(request,'mysite3/todays_deals.html')
	
def discover(request):
    return render(request,'mysite3/discover.html')
	
def about(request):
    return render(request,'mysite3/about.html')
	
def contact(request):
    return render(request,'mysite3/contact.html')
	
def genres(request):
    return render(request,'mysite3/genres.html')

def categories(request):
    return render(request,'mysite3/categories.html')
	
#categories
def youngadult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE category="Young Adult" order by title');
    return render(request,'mysite3/category_s/youngadult.html',{'yadata':yadata})
	
def kids(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE category="Kids" order by title');
    return render(request,'mysite3/category_s/youngadult.html',{'yadata':yadata})
	
def newadult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE category="New Adult" order by title');
    return render(request,'mysite3/category_s/youngadult.html',{'yadata':yadata})
	
def adult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE category="Adult" order by title');
    return render(request,'mysite3/category_s/youngadult.html',{'yadata':yadata})

#genres	
def contemporary(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="Contemporary" order by title');
    return render(request,'mysite3/genre_s/contemporary.html',{'data':data})
	
def mysteryandcrime(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="mystery & crime" order by title');
    return render(request,'mysite3/genre_s/mysteryandcrime.html',{'data':data})
	
def thriller(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="thriller" order by title');
    return render(request,'mysite3/genre_s/thriller.html',{'data':data})

def sciencefiction(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="science fiction" order by title');
    return render(request,'mysite3/genre_s/sciencefiction.html',{'data':data})
	
def humour(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="humour" order by title');
    return render(request,'mysite3/genre_s/humour.html',{'data':data})
	
def fantasy(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="fantasy" order by title');
    return render(request,'mysite3/genre_s/fantasy.html',{'data':data})
	
def romance(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="romance" order by title');
    return render(request,'mysite3/genre_s/romance.html',{'data':data})
	
def chicklit(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="chick lit" order by title');
    return render(request,'mysite3/genre_s/chicklit.html',{'data':data})
	
def dystopia(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="dystopia" order by title');
    return render(request,'mysite3/genre_s/dystopia.html',{'data':data})
	
def nonfiction(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="non fiction" order by title');
    return render(request,'mysite3/genre_s/nonfiction.html',{'data':data})
	
def horror(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="horror" order by title');
    return render(request,'mysite3/genre_s/horror.html',{'data':data})
	
def textbooks(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="textbooks" order by title');
    return render(request,'mysite3/genre_s/textbooks.html',{'data':data})
	
def poetry(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="poetry" order by title');
    return render(request,'mysite3/genre_s/poetry.html',{'data':data})
	
def comics(request):
    data = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE genre="comics" order by title');
    return render(request,'mysite3/genre_s/comics.html',{'data':data})
	
#books
def warcross(request):
    return render(request,'mysite3/books/warcross.html')