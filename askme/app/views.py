from django.http import HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
import random

from app.models import *

new_questions = Question.new_questions.all()
hot_questions = Question.hot_questions.all()
top_tags = Tag.top_tags.all()
top_users = Profile.top_users.all()
# Create your views here.
QUESTIONS = [
    {
        "title": f"Question #{i}",
        "text": f"Text of question #{i}",
        "number": i,
        "tag1": f"Teg #{i}",
        "tag2": f"Teg #{i+1}",
        "likes":  random.randint(1,50)
    } for i in range(10)
]


ANSWERS = [
    {
        "text": f"Text of answer #{i}",
        "likes":  random.randint(1,50),
    } for i in range(5)
]


TAGS = [
    {
        "tag": f"Teg #{i}",
    } for i in range(11)
]


def index(request):
    questions = paginate(new_questions, request)
    context = {
        "questions": questions,
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "index.html", context)


def hot(request):
    questions = paginate(hot_questions, request)
    context = {
        "questions": questions,
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "hot.html", context)


def tags(request, tag_f: str):
    tagg = get_object_or_404(Tag.tags.filter(tag=tag_f)).questions.all()
    questions = paginate(tagg, request)
    context = {
        "questions": questions,
        "teg_filt": tag_f,
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "tags.html", context)


def question(request,i: int):
    question = get_object_or_404(Question, pk = i)
    answers = Answer.answers.filter(question=question)
    answers = paginate(answers, request)
    context = {
        "question": question,
        "answers": answers,
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "question.html", context)


def login(request):
    context = {
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "login.html", context)


def signup(request):
    context = {
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "signup.html", context)


def ask(request):
    context = {
        "top_tegs": top_tags,
        "top_users":top_users}
    return render(request, "ask.html", context)

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    objects_on_page = paginator.get_page(page)
    return objects_on_page

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Not found!</h1>')