from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Authors, Cart, Discount, Users
from django.views import generic
import datetime
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
globalemail = None

# Create your views here.

def search(request):
    if request.method == 'POST':
        book_name =  request.POST.get('search')
        book = Books.objects.filter(title__icontains=book_name)
        return render(request,"mysite3/search.html",{'data':book})
    if request.method == 'GET':
        return render(request,'mysite3/new_releases.html',{})

def index(request):
    return render(request,'mysite3/login.html')
	
def sign_up(request):
    if request.method == 'POST':
        uemail =  request.POST.get('email')
        upwd =  request.POST.get('password')
        upwdag =  request.POST.get('passwordagain')
        if upwd == upwdag :
            data = Users.objects.raw('INSERT INTO Users values("%s","%s")',[uemail,upwd])
            return render(request,"mysite3/login.html",{})
        else :
            return render(request,'mysite3/sign_up.html',{})
    if request.method == 'GET':
        return render(request,'mysite3/sign_up.html',{})
	

def nr_login(request):
    if request.method == 'POST':
        uemail =  request.POST.get('email')
        upwd =  request.POST.get('password')
        temail = Users.objects.raw('SELECT * from Users')
        for i in temail:
            if Users.objects.filter( email = uemail, pwd=upwd ).exists() :
                end_date = datetime.datetime.now()
                start_date = end_date - datetime.timedelta(days=365)
                global globalemail
                globalemail = uemail
                data  = Books.objects.filter(pub_date__range=(start_date, end_date))
                return render(request,'mysite3/new_releases.html',{'data':data})
        return render(request,'mysite3/login_again.html')
    if request.method == 'GET':
        return render(request,'mysite3/login.html',{})

def new_releases(request):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=365)
    data = Books.objects.filter(pub_date__range=(start_date, end_date))
    return render(request,'mysite3/new_releases.html',{'data':data})
	
def cart(request):
    global globalemail
    totalprice = 0
    data = Books.objects.raw('(SELECT b.isbn,b.title,b.cover,a.a_name,b.format,d.dprice as "price" FROM authors a, books b, cart c, discount d WHERE c.isbn=b.isbn and c.isbn=d.isbn and b.a_id=a.a_id and c.email=%s) UNION (SELECT b.isbn,b.title,b.cover,a.a_name,b.format,b.price FROM authors a,books b,cart c where c.isbn=b.isbn and b.a_id=a.a_id and c.email=%s and c.isbn NOT IN (select isbn from discount))',[globalemail,globalemail]);
    for i in data:
        totalprice = totalprice + i.price
    price = {
        'pr':totalprice
    }
    return render(request,'mysite3/cart.html',{'data':data,'price':price})
	
'''def delbook(request, *args, **kwargs):
    from django.db import connection, transaction
    cursor = connection.cursor()
    viewbook = kwargs['bookname']
    global globalemail
    data = Books.objects.raw('SELECT * FROM Books natural join Authors where isbn=%s',[viewbook])
    return render(request,'mysite3/cart.html',{'data':data})'''
	
def delcart(request, *args, **kwargs):
    from django.db import connection, transaction
    cursor = connection.cursor()
    delbook = kwargs['bookname']
    global globalemail
    res = cursor.execute('call cartdel(%s,%s)',[globalemail,delbook])
    totalprice = 0
    data = Books.objects.raw('(SELECT b.isbn,b.title,b.cover,a.a_name,b.format,d.dprice as "price" FROM authors a, books b, cart c, discount d WHERE c.isbn=b.isbn and c.isbn=d.isbn and b.a_id=a.a_id and c.email=%s) UNION (SELECT b.isbn,b.title,b.cover,a.a_name,b.format,b.price FROM authors a,books b,cart c where c.isbn=b.isbn and b.a_id=a.a_id and c.email=%s and c.isbn NOT IN (select isbn from discount))',[globalemail,globalemail]);
    for i in data:
        totalprice = totalprice + i.price
    price = {
        'pr':totalprice
    }
    return render(request,'mysite3/cart.html',{'data':data,'price':price})
	
def todays_deals(request):
    data = Books.objects.raw('SELECT * FROM Discount natural join Books order by offer desc');
    return render(request,'mysite3/todays_deals.html',{'data':data})
	
def discover(request):
    data = Books.objects.raw('SELECT * FROM Books WHERE avg_rating>4');
    return render(request,'mysite3/discover.html',{'data':data})
	
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
    return render(request,'mysite3/category_s/kids.html',{'yadata':yadata})
	
def newadult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE category="New Adult" order by title');
    return render(request,'mysite3/category_s/newadult.html',{'yadata':yadata})
	
def adult(request):
    yadata = Books.objects.raw('SELECT * FROM Books natural join AUTHORS WHERE category="Adult" order by title');
    return render(request,'mysite3/category_s/adult.html',{'yadata':yadata})

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
    return render(request,'mysite3/genre_s/comics.html',{'data' :data})
	
#books
#book when not added to cart
def book(request, *args, **kwargs):
    global globalemail
    global viewbook
    viewbook = kwargs['bookname']
    data = Books.objects.raw('(SELECT b.isbn,b.cover,b.format,b.title,b.category,b.genre,b.synopsis,d.dprice as "price",a.a_name FROM books b, authors a, discount d WHERE b.a_id=a.a_id and b.isbn=d.isbn and b.isbn=%s) UNION (SELECT b.isbn,b.cover,b.format,b.title,b.category,b.genre,b.synopsis,b.price as "price",a.a_name FROM books b, authors a WHERE b.a_id=a.a_id and b.isbn NOT IN (select isbn from discount) and b.isbn=%s)',[viewbook,viewbook]);
    if Cart.objects.filter( isbn = viewbook, email = globalemail ).exists() :
        return render(request,'mysite3/book2.html',{'data':data})
    else :
        return render(request,'mysite3/book.html',{'data':data})

#book when added to cart
def book2(request):
    from django.db import connection, transaction
    cursor = connection.cursor()
    global viewbook
    global globalemail
    cursor.execute('INSERT INTO Cart values(%s,%s)',[viewbook,globalemail])
    data = Books.objects.raw('(SELECT b.isbn,b.cover,b.format,b.title,b.category,b.genre,b.synopsis,d.dprice as "price",a.a_name FROM books b, authors a, discount d WHERE b.a_id=a.a_id and b.isbn=d.isbn and b.isbn=%s) UNION (SELECT b.isbn,b.cover,b.format,b.title,b.category,b.genre,b.synopsis,b.price as "price",a.a_name FROM books b, authors a WHERE b.a_id=a.a_id and b.isbn NOT IN (select isbn from discount) and b.isbn=%s)',[viewbook,viewbook]);
    return render(request,'mysite3/book2.html',{'data':data})