from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('api/books/', views.BookListCreate.as_view()),
    path('api/books/<int:pk>', views.SingleBook.as_view()),
    path('api/books/<str:title>/', views.GetByTitle.as_view()),
    path('api/categories/<str:categories>/', views.GetByCategories.as_view()),
    path('api/authors/<str:title>/', views.GetByAuthors.as_view()),
    path('api/series/<str:title>/', views.GetBySeries.as_view()),
    path('api/labels/<str:title>/', views.GetByLabels.as_view())
]
