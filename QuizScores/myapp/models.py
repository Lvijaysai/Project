

# Create your models here.

from django.db import models

class ScoreRecord(models.Model):
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)