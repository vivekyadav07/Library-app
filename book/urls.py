from django.contrib import admin
from django.urls import path
from book import views


urlpatterns = [
   path('' ,views.index),
   path('booklist1/',views.BookListView,name="booklist1"),

   path("add_book/", views.add_book, name="add_book"),
   #path('book/<int:pk>/update/', views.BookUpdate, name='book_update'),
   #path('book/<int:pk>/delete/', views.BookDelete, name='book_delete'),

   path("delete_book/<int:myid>/", views.delete_book, name="delete_book"), 
   path('search/', views.searchposts, name='searchposts'),


]
