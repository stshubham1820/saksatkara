from .assessment_model import Assessment
from django.db import models
from user_authentication.models import User

class AssessmentQuestions(models.Model):
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='assessment_questions')
    question = models.TextField()
    marks = models.DecimalField(max_digits=5,decimal_places=2)


class AssessmentAnswers(models.Model):
    question = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='question_answers')
    answers = models.TextField()
    given_marks = models.DecimalField(max_digits=5,decimal_places=2)
    given_by = models.ForeignKey(User,on_delete=models.CASCADE)
