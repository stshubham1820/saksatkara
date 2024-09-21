from django.db import models
from .question_answer_models import AssessmentAnswers

class Transcript(models.Model):
    assessment_transcript = models.OneToOneField(AssessmentAnswers, on_delete=models.CASCADE,related_name='assessment_transcript')
    raw_transcript = models.TextField()
    json_transcript = models.TextField()

    class Meta:
        db_table = 'transcript'