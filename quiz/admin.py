from django.contrib import admin
from .models import Category, Quiz, Question

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'text', 'answer1', 'answer2', 'answer3', 'answer4', 'correct_answer')
    list_display_links = ('id', 'quiz')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)