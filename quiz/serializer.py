from rest_framework import serializers
from .models import (
    Category,
    Quiz,
    Question,
    TempUser,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class QuizSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    questions_count = serializers.IntegerField(source='count_questions_by_category', read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'name', 'category', 'category_id', 'questions_count')

class DisplayQuizzesWithQuestions(serializers.ModelSerializer):
    quiz = serializers.CharField(source="quiz.name", read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'quiz', 'text', 'answer1', 'answer2', 'answer3', 'answer4')


class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.CharField(source='quiz.name', read_only=True)
    quiz_id = serializers.IntegerField(source='quiz.id', read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'quiz', 'quiz_id', 'text', 'answer1', 'answer2', 'answer3', 'answer4')

class TempUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempUser
        fields = ('id', 'name', 'username',)


class DetailQuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    questions_count = serializers.IntegerField(source='count_questions_by_category', read_only=True)


    class Meta:
        model = Quiz
        fields = ('id', 'name', 'category', 'category_id', 'questions', 'questions_count', )

class DisplayQuestionsByQuizID(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'quiz', 'text', 'answer1', 'answer2', 'answer3', 'answer4')

class DetailQuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    name = serializers.CharField(source='quiz.name', read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'quiz', 'text', 'answer1', 'answer2', 'answer3', 'answer4', 'name')

class DetailTempUserSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = TempUser
        fields = ('id', 'name', 'username', 'quiz', 'questions', )

class DetailCategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'quizzes')

