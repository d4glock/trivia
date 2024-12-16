# questions/models.py
from django.db import models
import random

class Question(models.Model):
    text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_shuffled_options(self):
        options = [
            {'text': self.option_1, 'is_correct': self.option_1 == self.correct_answer},
            {'text': self.option_2, 'is_correct': self.option_2 == self.correct_answer},
            {'text': self.option_3, 'is_correct': self.option_3 == self.correct_answer},
            {'text': self.option_4, 'is_correct': self.option_4 == self.correct_answer},
        ]
        random.shuffle(options)
        return options

    class Meta:
        ordering = ['?']