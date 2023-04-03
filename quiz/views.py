from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import (
    Category,
    Quiz,
    Question,
    TempUser,
)
from .serializer import (
    CategorySerializer,
    QuizSerializer,
    QuestionSerializer,
    TempUserSerializer,
    DisplayQuizzesWithQuestions,
    DetailQuestionSerializer,
    DetailTempUserSerializer,
    DetailCategorySerializer,
    DisplayQuestionsByQuizID,
)
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def quizzes(self, request, pk=None):
        category = self.get_object()
        serializer = DetailCategorySerializer(category)
        return Response(serializer.data)
    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


    @action(detail=True, methods=['get'])
    def retrieve(self, request, *args, **kwargs):
        query = Question.objects.filter(quiz=self.get_object())
        serializer = DisplayQuizzesWithQuestions(query, many=True)
        try:
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": f"{e}"})

        
    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        quiz = self.get_object()
        questions = Question.objects.filter(quiz=quiz)
        serializer = DisplayQuestionsByQuizID(questions, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def get_quiz_by_category(self, request, category, *args, **kwargs):
        if request.method == 'GET':
            query = Quiz.objects.filter(category__name=category)
            return Response(self.serializer_class(query, many=True).data)
        return Response("Another method requested")
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['get'])
    def quiz(self, request, pk=None):
        question = self.get_object()
        serializer = DetailQuestionSerializer(question)
        
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def search(self, request, search, *args, **kwargs):
        print('search', search)
        if request.method == 'GET':
            query = Question.objects.filter(Q(text__icontains=search) | Q(answer1__icontains=search) | Q(answer2__icontains=search) | Q(answer3__icontains=search) | Q(answer4__icontains=search) | Q(quiz__category__name__icontains=search) | Q(quiz__name__icontains=search))
            if query.count() == 0:
                return Response({"error": "No results found"}, status=204)
            
            return Response(self.serializer_class(query, many=True).data)
    
class TempUserViewSet(viewsets.ModelViewSet):
    queryset = TempUser.objects.all()
    serializer_class = TempUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = TempUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# View to take a quiz. Post the answers to the questions.

from rest_framework.views import APIView

class TakeQuizView(APIView):
    def get(self, request, *args, **kwargs):
        query = Question.objects.all()
        serializer = DetailQuestionSerializer(query, many=True)       # serializer.is_valid()
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                '1': openapi.Schema(type=openapi.TYPE_STRING),
                '2': openapi.Schema(type=openapi.TYPE_STRING),
                '3': openapi.Schema(type=openapi.TYPE_STRING),
                '4': openapi.Schema(type=openapi.TYPE_STRING),
                '5': openapi.Schema(type=openapi.TYPE_STRING),
                '6': openapi.Schema(type=openapi.TYPE_STRING),
                '7': openapi.Schema(type=openapi.TYPE_STRING),
                '8': openapi.Schema(type=openapi.TYPE_STRING),
                '9': openapi.Schema(type=openapi.TYPE_STRING),
                '10': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'score': openapi.Schema(type=openapi.TYPE_INTEGER),
                'total': openapi.Schema(type=openapi.TYPE_INTEGER),
            }
        )},

    )
    def post(self, request, *args, **kwargs):
        simple_req_body = [
            {
                "question": "Question name 1",
                "answer": "answer1"
            },
            {
                "question": "Question name 2",
                "answer": "answer2"
            },

        ]
        answers = request.data.get('answers', None)
        if answers is None:
            return Response({'error': 'No answers provided', 'example_request_body': simple_req_body}, status=400)
        
        score = 0
        total = 0
        print(answers)
        for answer in answers:
            question = Question.objects.get(text=answer['question'])
            correct_answer = question.get_correct_answer()
            print(correct_answer, answer['answer'], correct_answer == answer['answer'], sep=' | ')
            if correct_answer == answer['answer']:
                score += 1
            total += 1
        # quiz = Quiz.objects.get(id=kwargs['pk'])
        # questions = Question.objects.filter(quiz=quiz)
        # for question in questions:
        #     total += 1
            # correct_answer = question.get_correct_answer()

        return Response({'score': score, 'total': total})
    

