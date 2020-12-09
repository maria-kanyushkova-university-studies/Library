from rest_framework import generics

from .models import Book
from book.serializers import BookSerializer


# def index(request):
#     # b = Book(title="title", description="description", rate="0", isbn="isbn")
#     # b.save()
#     return HttpResponse("Hello, world. You're at the books index.")


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def perform_create(self, serializer):
    #    title = generics.get_object_or_404()
    #    return serializer.save(title=title)


class SingleBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
