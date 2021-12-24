from django.contrib import admin
from django.urls import path
from book import views
from .views import SearchResultsListView

urlpatterns = [
   path('' ,views.index),
   path('booklist1/',views.BookListView,name="booklist1"),
   path('topval/',views.BookListView1,name="topval"),
   path('top/',views.BookListView2,name="top"),
   path("add_book/", views.add_book, name="add_book"),
   path("update_data/<int:id>/", views.update_data, name='update_data'),
   
   path("delete_book/<int:myid>/", views.delete_book, name="delete_book"), 
   
   path('search/', SearchResultsListView.as_view(), name = 'search_results'),

]
