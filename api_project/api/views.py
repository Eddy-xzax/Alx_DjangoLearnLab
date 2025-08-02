from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer 
from bookshelf.models import Book
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializery_class = BookSerializer
