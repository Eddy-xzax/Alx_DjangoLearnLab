from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()

router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('',include(router.urls)),
]
