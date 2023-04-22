from rest_framework import viewsets

from biblioteca.models import Book, Author
from biblioteca.serializers import BookSerializer, AuthorSerializer


# Create your views here.


class AuthorViewsSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewsSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
