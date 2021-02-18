from rest_framework import serializers

from bookstore.models import Book, Publisher, Author, BookAuthor


class PubNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    publisher = PubNameSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'cover_image', 'publisher']


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['firstname', 'lastname']


class BookAuthorSerializer(serializers.ModelSerializer):
    writer = AuthorInfoSerializer(source='author', read_only=True)

    class Meta:
        model = BookAuthor
        fields = ['writer']


class BookDetailSerializer(serializers.ModelSerializer):
    publisher = PubNameSerializer(read_only=True)
    authors_list = BookAuthorSerializer(source='authors', many=True, read_only=True)
    cover_image = serializers.ImageField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'cover_image', 'publisher', 'pages_num', 'authors_list']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'nickname', 'birthdate']


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class BookListSerializer(serializers.ModelSerializer):
    book_title = BookInfoSerializer(source='book')

    class Meta:
        model = BookAuthor
        fields = ['book_title']


class AuthorDetailSerializer(serializers.ModelSerializer):
    books_list = BookListSerializer(source='books', many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'nickname', 'books_list']
