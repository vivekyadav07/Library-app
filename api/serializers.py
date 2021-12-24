# api/serializers.py
from re import ASCII
from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.Serializer):
    id=serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=20)
    author = serializers.CharField(max_length=10)
    summary = serializers.CharField(max_length=10)
    isbn = serializers.CharField(max_length=13)
   
'''class BookSerializer(serializers.Serializer):

    class Meta:
        model = Book
        fields = ['title', 'author','summary', 'isbn']'''
