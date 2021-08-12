from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(default='', max_length=1024)
    text = models.TextField(default='')
    added_at = models.DateField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User,related_name="q_to_likes")

    def __str__(self):
      return self.title
    
    def get_url(self):
      return "/questions/{}/".format(self.id)

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')

class Answer(models.Model):
    text = models.TextField(default='')
    added_at = models.DateField(null=True)
    question = models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
