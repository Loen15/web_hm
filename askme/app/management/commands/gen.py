from django.core.management.base import BaseCommand
from app.models import Profile, Question, Answer, Tag
from django.contrib.auth.models import User
import random, string

class Command(BaseCommand):
    user_numbers = 1000
    questions_numbers = 10000
    answers_numbers = 100000
    tags_numbers = 1000

    avatars_set = [
        'img/avat1.jpg', 'img/avat2.jpg', 'img/avat3.jpg', 'img/avatar.jpg'
    ]

    def generate_text(min, max, len):
            if min < max:
                count_worlds = random.randrange(min, max, 1)
            else:
                count_worlds = min
            text = ""
            for j in range(count_worlds):
                rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(len))
                text = text + rand_string + ' '
            return text

#
    #generate answers
    for i in range(answers_numbers):
        text = generate_text(30,200,random.randrange(3, 10, 1))
        author = random.choice(User.objects.all())
        is_correct = random.choice(['True', 'False'])
        likes = random.randint(0,100)
        question = random.choice(Question.new_questions.all())
        answer = Answer(text = text, author = author, is_correct = is_correct, likes = likes, question = question)
        answer.save()
    print("answers created")
    def handle(self, *args, **options):
        import this
