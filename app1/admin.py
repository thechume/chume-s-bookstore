from django.contrib import admin

# Register your models here.

#from .models import Question
from app1.models import Authors, Books, Cart, Discount, Users
#admin.site.register(Question)
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Cart)
admin.site.register(Discount)
admin.site.register(Users)
