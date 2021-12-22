# api/serializers.py
from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    author = serializers.CharField(max_length=10)
    summary = serializers.CharField(max_length=10)
    isbn = serializers.CharField(max_length=13)
   
   
''' class Meta:
        model = Book
        fields = ('title', 'author','summary', 'isbn')'''
