from django.http import HttpResponse

from book.models import Book


def index(request):
    b = Book(title="title", description="description", rate="0", isbn="isbn")
    b.save()
    return HttpResponse("Hello, world. You're at the books index.")
