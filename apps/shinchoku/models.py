from django.db import models
from django.contrib.auth.models import User


class Shinchoku(models.Model):
    user = models.ForeignKey(User,
                             related_name='Shinchokus',
                             on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
