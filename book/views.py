from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import  ListView

#from .forms import Bookform

#Create your views here.

# HOME PAGE
def index(request):
    book_list = Book.objects.all()
    context ={'booklist':book_list}
    return render(request,'index.html',context)





# VIEW THAT WILL RETURN LIST OF ALL BOOKS IN LIBRARY
def BookListView(request):
    book_list = Book.objects.all()
    context ={'booklist':book_list}
    # MODELNAME.objects.all() is used to get all objects i.e. tuples from database
    return render(request, 'book_list.html', context)



#ADD BOOK

def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        summary = request.POST.get('summary')
        isbn = request.POST['isbn']
       

        books = Book.objects.create(title=title, author=author,summary=summary,isbn=isbn)
        books.save()
       
       
    return render(request, "add_book.html")


  #UPDATE BOOK
def update_data(request,id):


    if request.method == "POST":

        pi=Book.objects.get(pk=id)
        fm =Bookform(request.POST,instance=pi)
        if fm.is_valid():
         fm.save()

    else:


        pi=Book.objects.get(pk=id)
        fm =Bookform(instance=pi)
    return render (request,'update_data.html',{'form':fm})       

    

       
'''title = request.POST['title']
        author = request.POST['author']
        summary = request.POST.get('summary')
        isbn = request.POST['isbn']
       

        books = Book.objects.create(title=title, author=author,summary=summary,isbn=isbn)
        books.save()
   
 

       
    return render(request, "add_book.html")'''





#DELETE BOOK

def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/booklist1")


#SEARCH WORDS 
'''   
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(author__icontains=query)

            results= Book.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

'''


