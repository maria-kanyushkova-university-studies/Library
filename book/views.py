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
