from django.urls import path
from .views import (
    QuizViewSet,
    CategoryViewSet,
    QuestionViewSet,
    TempUserViewSet,
    TakeQuizView,
)

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('categories/<int:pk>/quizzes/', CategoryViewSet.as_view({'get': 'quizzes'})),
    path('quizzes/', QuizViewSet.as_view({'get': 'list'})),
    path('quizzes/by-category/<str:category>/', QuizViewSet.as_view({'get': 'get_quiz_by_category'}), name='quizzes-by-category'),
    path('quizzes/<int:pk>/', QuizViewSet.as_view({'get': 'retrieve'})),
    path('quizzes/<int:pk>/questions/', QuizViewSet.as_view({'get': 'questions'})),
    path('questions/', QuestionViewSet.as_view({'get': 'list'})),
    path('questions/<str:search>/', QuestionViewSet.as_view({'get': 'search'})),
    path('questions/<int:pk>/', QuestionViewSet.as_view({'get': 'retrieve'})),
    path('questions/<int:pk>/quiz/', QuestionViewSet.as_view({'get': 'quiz'})),
    path('tempuser/', TempUserViewSet.as_view({'get': 'list'})),
    # create a new temp user
    path('tempuser/create/', TempUserViewSet.as_view({'post': 'create'})),
    path('tempuser/<int:pk>/', TempUserViewSet.as_view({'get': 'retrieve'})),

    # View to take a quiz. Post the answers to the questions.
    path('takequiz/', TakeQuizView.as_view()),
]
