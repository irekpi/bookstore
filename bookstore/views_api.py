from rest_framework import viewsets
from bookstore.models import Book, Author, Publisher
from bookstore.serializers import AuthorDetailSerializer, AuthorSerializer, BookSerializer, PublisherSerializer, \
    BookDetailSerializer
from rest_framework import viewsets

from bookstore.models import Book, Author, Publisher
from bookstore.serializers import AuthorDetailSerializer, AuthorSerializer, BookSerializer, PublisherSerializer, \
    BookDetailSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter()
    serializer_class = BookDetailSerializer
    serializer_action_class = {
        'list': BookSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_class[self.action]
        except:
            return super(BooksViewSet, self).get_serializer_class()


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.filter()
    serializer_class = PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter()
    serializer_class = AuthorDetailSerializer
    serializer_action_class = {
        'list': AuthorSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_class[self.action]
        except:
            return super(AuthorViewSet, self).get_serializer_class()
