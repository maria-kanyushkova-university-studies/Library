from django.contrib import admin

from book.models import Asset, Author, Publisher, Label, Category, Series, Purchase, Book, Wishlist, Code, ReadingBook, \
    Comment

admin.site.register(Asset)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Series)
admin.site.register(Purchase)
admin.site.register(Book)
admin.site.register(Wishlist)
admin.site.register(Code)
admin.site.register(ReadingBook)
admin.site.register(Comment)