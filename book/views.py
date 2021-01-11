from rest_framework import generics

from .models import Book
from book.serializers import BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def perform_create(self, serializer):
    #    title = generics.get_object_or_404()
    #    return serializer.save(title=title)


class SingleBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GetByTitle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = 'title'
    queryset = Book.objects.all()


class GetByCategories(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = 'categories'
    queryset = Book.objects.all()


class GetByAuthors(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = 'authors'
    queryset = Book.objects.all()


class GetBySeries(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = 'series'
    queryset = Book.objects.all()


class GetByLabels(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = 'labels'
    queryset = Book.objects.all()


