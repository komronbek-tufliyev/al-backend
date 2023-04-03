from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    # identifier = models.CharField(max_length=255, verbose_name=_('Identifier'), unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.name
    
    def count_questions_by_category(self):
        return str(Question.objects.filter(quiz=self.pk).count())
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    text = models.CharField(max_length=255, verbose_name=_('Text'))
    answer1 = models.CharField(max_length=255, verbose_name=_('Answer 1'))
    answer2 = models.CharField(max_length=255, verbose_name=_('Answer 2'))
    answer3 = models.CharField(max_length=255, verbose_name=_('Answer 3'))
    answer4 = models.CharField(max_length=255, verbose_name=_('Answer 4'))

    CORRECT_ANSWER_CHOICES = (
        ('1', 'Answer 1'),
        ('2', 'Answer 2'),
        ('3', 'Answer 3'),
        ('4', 'Answer 4'),
    )
    correct_answer = models.CharField(max_length=1, choices=CORRECT_ANSWER_CHOICES, verbose_name=_('Correct Answer'), default='1')

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.text

    def get_correct_answer(self):
        c_a = int(self.correct_answer)
        return {
            1: self.answer1,
            2: self.answer2,
            3: self.answer3,
            4: self.answer4,
        }.get(c_a, 'Invalid answer')
    
    def get_answers(self):
        return [self.answer1, self.answer2, self.answer3, self.answer4]
    
    def get_answers_with_correct(self):
        answers = self.get_answers()
        answers[int(self.correct_answer) - 1] = f'{answers[int(self.correct_answer) - 1]} (correct)'
        return answers

    
class TempUser(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    username = models.CharField(max_length=255, verbose_name=_('Username'), unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Temp User')
        verbose_name_plural = _('Temp Users')

    def __str__(self):
        return self.username


class QuizTaker(models.Model):
    user = models.ForeignKey(TempUser, on_delete=models.CASCADE, verbose_name=_('User'), null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    score = models.IntegerField(verbose_name=_('Score'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Quiz Taker')
        verbose_name_plural = _('Quiz Takers')

    def __str__(self):
        return f'{self.user.username} - {self.quiz.name}'
    

    

