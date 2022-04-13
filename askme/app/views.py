from django.core.paginator import Paginator
from django.shortcuts import render
import random

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
    questions = paginate(QUESTIONS, request)
    context = {
        "questions": questions,
        "tags": TAGS}
    return render(request, "index.html", context)


def hot(request):
    questions = paginate(QUESTIONS, request)
    context = {
        "questions": questions,
        "tags": TAGS}
    return render(request, "hot.html", context)


def tags(request, tag: str):
    questions = paginate(QUESTIONS, request)
    context = {
        "tag": tag,
        "questions": questions,
        "tags": TAGS}
    return render(request, "tags.html", context)


def question(request,i: int):
    answers = paginate(ANSWERS, request)
    context = {
        "question": QUESTIONS[i],
        "answers": answers,
        "tags": TAGS}
    return render(request, "question.html", context)


def login(request):
    context = {"tags": TAGS}
    return render(request, "login.html", context)


def signup(request):
    context = {"tags": TAGS}
    return render(request, "signup.html", context)


def ask(request):
    context = {"tags": TAGS}
    return render(request, "ask.html", context)

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    objects_on_page = paginator.get_page(page)
    return objects_on_page