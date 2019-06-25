from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=400)
    image_text = models.CharField(max_length=50)
    question_key = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
    # def get(self):
    #     return self.question_text
