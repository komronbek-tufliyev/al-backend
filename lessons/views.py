from rest_framework import generics, views, status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Q, Count


from .models import (
    Book,
    Archive,
    Topic,
)

from quiz.models import Category

from .serializers import (
    CategorySerializer,
    BookSerializer,
    ArchiveSerializer,
    TopicSerializer,
)

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class ArchiveList(generics.ListAPIView):
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()

class TopicList(generics.ListAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BookDetail(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class ArchiveDetail(generics.RetrieveAPIView):
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()

class TopicDetail(generics.RetrieveAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class CategoryBooks(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        return Book.objects.filter(category=category)
    
class CategoryArchives(generics.ListAPIView):
    serializer_class = ArchiveSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        return Archive.objects.filter(category=category)
    
class CategoryTopics(generics.ListAPIView):
    serializer_class = TopicSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        return Topic.objects.filter(category=category)
    
class SearchView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        search_result = None
        query = self.kwargs['query']
        search_result = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        if not search_result:
            search_result = Archive.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        if not search_result:
            search_result = Topic.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return search_result
    
class SearchBookView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        search_result = None
        query = self.kwargs['query']
        search_result = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return search_result
    
class SearchArchiveView(generics.ListAPIView):
    serializer_class = ArchiveSerializer
    def get_queryset(self):
        search_result = None
        query = self.kwargs['query']
        search_result = Archive.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return search_result
    
class SearchTopicView(generics.ListAPIView):
    serializer_class = TopicSerializer
    def get_queryset(self):
        search_result = None
        query = self.kwargs['query']
        search_result = Topic.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return search_result
    
    
    
