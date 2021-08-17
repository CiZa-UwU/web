from qa.forms import AskForm
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Question(models.Model):
    title = models.CharField(default="", max_length=1024)
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0,null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.pk})


class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text