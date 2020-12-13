from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('api/books/', views.BookListCreate.as_view()),
    path('api/books/<int:pk>', views.SingleBook.as_view())
]
