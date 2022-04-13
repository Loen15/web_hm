from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tagManager(models.Manager):
    def get_queryset(self):
        return super(tagManager,self).get_queryset().order_by('-count')[:10]

class Tag(models.Model):
    tag = models.CharField(max_length=15, unique=True)
    count = models.IntegerField(null=True)

    tags = models.Manager()        
    top_tags = tagManager()

    
    class Meta:
        ordering = ["tag"]


class profileManager(models.Manager):
    def get_queryset(self):
        return super(profileManager,self).get_queryset().order_by('-likes')[:5]
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar = models.ImageField(upload_to=".")
    likes = models.IntegerField(null=True)
    
    
    users = models.Manager()
    top_users = profileManager()
    class Meta:
        ordering = ['-likes']


class questionManager(models.Manager):
    def get_queryset(self):
        return super(questionManager,self).get_queryset().order_by('-likes')



class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=65000)
    tag = models.ManyToManyField(Tag, related_name='questions')
    likes = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
  
    new_questions = models.Manager()
    hot_questions = questionManager()

    class Meta:
        ordering = ["date"]


class Answer(models.Model):
    text = models.CharField(max_length=65000)
    likes = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answers')

    answers = models.Manager()

    class Meta:
        ordering = ["-likes","-is_correct"]