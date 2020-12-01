from django.contrib.auth.models import User
from django.db import models


class Asset(models.Model):
    filename = models.UUIDField(primary_key=True)
    extension = models.CharField(max_length=10)
    path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    # filename = models.UUIDField()


class Publisher(models.Model):
    title = models.CharField(max_length=255)
    # filename = models.UUIDField()


class Label(models.Model):
    title = models.CharField(max_length=255)


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Series(models.Model):
    title = models.CharField(max_length=255)


class Purchase(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    link = models.TextField()
    comment = models.TextField()
    is_actual = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    isbn = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    authors = models.ManyToManyField(Author)
    labels = models.ManyToManyField(Label)
    categories = models.ManyToManyField(Category)
    series = models.ManyToManyField(Series)
    publishers = models.ManyToManyField(Publisher)
    # assets = models.ManyToManyField(Asset, related_name="assets")
    # ebooks = models.ManyToManyField(Asset, related_name="ebook")


class Wishlist(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_actual = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Code(models.Model):
    code = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReadingBook(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_actual = models.BooleanField(default='true')
    started_day = models.DateTimeField(auto_now_add=True)
    finished_day = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    description = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
