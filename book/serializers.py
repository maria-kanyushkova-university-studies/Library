from rest_framework import serializers

from book.models import Book, Author, Publisher, Label, Category, Purchase


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'surname', 'name', 'patronymic']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'title']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'title', 'author', 'link', 'comment', 'is_actual', 'user']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'rate', 'isbn', 'authors', 'labels', 'categories', 'series',
                  'publishers']


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'book', 'user', 'is_actual']


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'code', 'book', 'is_deleted']


class ReadingBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'code', 'user', 'is_actual']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'description', 'book', 'user', 'rate']
