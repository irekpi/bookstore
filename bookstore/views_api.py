from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from bookstore.models import Book, Author, Publisher
from bookstore.serializers import AuthorDetailSerializer, AuthorSerializer, BookSerializer, BookDetailSerializer, \
    PublisherSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer


class BookView(APIView):
    def get_book(self, book_id):
        try:
            model = Book.objects.get(id=book_id)
            return model
        except Book.DoesNotExist:
            return

    def get(self, request, book_id):
        if not self.get_book(book_id):
            return Response("Book does not Exist")

        serializer = BookDetailSerializer(self.get_book(book_id))
        return Response(serializer.data)

    def put(self, request, book_id):
        if not self.get_book(book_id):
            return Response("Book does not Exist")
        model = Book.objects.get(id=book_id)
        serializer = BookDetailSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        if not self.get_book(book_id):
            return Response("user does not exist")
        model = self.get_book(book_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.filter()
    serializer_class = PublisherSerializer


class PublisherDetailView(APIView):
    def get_publisher(self, book_id):
        try:
            model = Publisher.objects.get(id=book_id)
            return model
        except Publisher.DoesNotExist:
            return

    def get(self, request, publisher_id):
        if not self.get_publisher(publisher_id):
            return Response("Publisher does not Exist")

        serializer = PublisherSerializer(self.get_publisher(publisher_id))
        return Response(serializer.data)

    def put(self, request, publisher_id):
        if not self.get_publisher(publisher_id):
            return Response("Publisher does not Exist")
        model = Publisher.objects.get(id=publisher_id)
        serializer = PublisherSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, publisher_id):
        if not self.get_publisher(publisher_id):
            return Response("Publisher does not exist")
        model = self.get_publisher(publisher_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter()
    serializer_class = AuthorSerializer


class AuthorDetailView(APIView):
    def get_author(self, author_id):
        try:
            model = Author.objects.get(id=author_id)
            return model
        except Author.DoesNotExist:
            return

    def get(self, request, author_id):
        if not self.get_author(author_id):
            return Response("Author does not Exist")

        serializer = AuthorDetailSerializer(self.get_author(author_id))
        return Response(serializer.data)

    def put(self, request, author_id):
        if not self.get_author(author_id):
            return Response("Author does not Exist")
        model = Author.objects.get(id=author_id)
        serializer = AuthorDetailSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, author_id):
        if not self.get_author(author_id):
            return Response("Author does not exist")
        model = self.get_author(author_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
