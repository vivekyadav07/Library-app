from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import  ListView

from django.db.models import Count
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
         return render(request, "update_data.html")
    
    else:
        pi=Book.objects.get(pk=id)
        fm =Bookform(instance=pi)
    return render (request,'update_data.html',{'form':fm})       

    



#DELETE BOOK

def delete_book( request,myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/booklist1")


#SEARCH WORDS 

class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): 
		query = self.request.GET.get('q')
		return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

'''def topval(request):
   
    Book.objects.values('id').annotate(title_count=Count('title')).order_by('-title_count')[:5]
   # book_ids = Book.objects.filter(author=author).values_list('id', 'title').order_by('title')
    top_records = (Book.objects.order_by('-title').filter(score__in=top_scores[:10]))'''

#TOP THREE VALUE
def BookListView1(request):
   # book_list = Book.objects.all()
    book_list = Book.objects.annotate(Count('isbn')).order_by('isbn__count')[:3]
  
    #print(book_list)
    context ={'booklist':book_list}
    return render(request, 'top.html', context)

#TOP VALUE
def BookListView2(request):
   # book_list = Book.objects.all()
    book_list2 = Book.objects.annotate(Count('isbn')).order_by('isbn__count')[:1]
    
    #print(book_list)
    context ={'booklist':book_list2}
    return render(request, 'top.html', context)