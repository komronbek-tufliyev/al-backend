from django.urls import path
from .views import (
    CategoryList,
    CategoryDetail,
    BookList,
    BookDetail,
    ArchiveList,
    ArchiveDetail,
    TopicList,
    TopicDetail,

    SearchView,
    SearchTopicView,
    SearchArchiveView,
    SearchBookView,

    # By category
    CategoryBooks,
    CategoryTopics,
    CategoryArchives,


)

# API endpoints

urlpatterns = [
    # Categories endpoints
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),

    # Books endpoints
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
    path('books/<str:category>/', CategoryBooks.as_view()),

    # Archives endpoints
    path('archives/', ArchiveList.as_view()),
    path('archives/<int:pk>/', ArchiveDetail.as_view()),
    path('archives/<str:category>/', CategoryArchives.as_view()),

    # Topics endpoints
    path('topics/', TopicList.as_view()),
    path('topics/<int:pk>/', TopicDetail.as_view()),
    path('topics/<str:category>/', CategoryTopics.as_view()),

    # Search endpoints
    path('search/', SearchView.as_view()),
    path('search/topics/', SearchTopicView.as_view()),
    path('search/archives/', SearchArchiveView.as_view()),
    path('search/books/', SearchBookView.as_view()),
]

