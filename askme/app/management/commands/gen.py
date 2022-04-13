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

    # generate profiles
    for i in range(user_numbers):
        user = User(username= generate_text(1,1,random.randrange(4, 15, 1)), password=generate_text(1,1,random.randrange(10, 15, 1)), is_staff=False, is_active=True, is_superuser=False)
        user.save()
        profile = Profile(user=user, avatar=random.choice(avatars_set))
        profile.save()
    print("profiles created")
    #generate tags
    uses_tag = []
    for i in range(tags_numbers):
        teg = generate_text(1,1, random.randrange(3, 6, 1))
        while teg in uses_tag:
            teg = generate_text(1,1, random.randrange(3, 6, 1))    
        uses_tag.append(teg)
        tag = Tag(tag = teg, count = random.randrange(0, 1000, 1))
        tag.save()
    print("tags created")
    #generate questions
    for i in range(questions_numbers):
        title = generate_text(3, 10,random.randrange(3, 10, 1))
        text = generate_text(20, 70,random.randrange(3, 10, 1))
        author = random.choice(User.objects.all())
        question = Question(title=title, text=text, author=author, likes = random.randrange(1, 10000, 1))
        question.save()
        count_tags = random.randrange(1, 5)
        for k in range(count_tags):
            question.tag.add(random.choice(Tag.tags.all()))
    print("questions created")
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
