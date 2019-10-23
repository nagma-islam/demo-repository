from django.shortcuts import render,redirect
from .models import Book
# Create your views here.
def index(request):
    book = Book.objects.all()
    context = {
        'book' : book
    }
    return render(request,'index.html',context)


def addBook(request):
    bname=request.GET['bookName']
    bauthor=request.GET['author']
    bprice=request.GET['price']

    books=Book(name=bname,author=bauthor,price=bprice)
    books.save()
    return redirect('/')


def editBook(request,id):
    book = Book.objects.get(pk=id)
    context={
        'book':book
    }
    return render(request,'update.html',context)

def updateBook(request, id):
    book = Book.objects.get(pk=id)
    book.name=request.GET['nbookName']
    book.author=request.GET['nauthor']
    book.price=request.GET['nprice']
    book.save()
    return redirect('/')