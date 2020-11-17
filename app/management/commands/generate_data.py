from django.core.management.base import BaseCommand, CommandError
from app.models import *
from random import choice
from faker import Faker
f = Faker()

# TODO: сделать генерацию ответов и вопросов в виде отдельных команд 
# (или решить проблему не заполнения созданных в данной команде вопросов ответами)

# как вариант сделать добавление вопроса и наполнение его ответами в рамках одной функции 
# и ее уже зацикливать

class Command(BaseCommand):
    help = 'Generates Data'

    def add_arguments(self, parser):
        parser.add_argument('generate_size', type=int)

    def handle(self, *args, **options):
        generate_size = options['generate_size']
        # self.add_users()
        # self.add_tags()
        # self.add_questions(generate_size)
        self.fill_questions_with_answers(generate_size)

    def add_marks(self, mark_object):
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        enum = [Mark.MarkType.LIKE, Mark.MarkType.DISLIKE]
        mark = Mark.objects.create(
            mark_type = choice(enum),
            content_object = mark_object,
            user_id = choice(users_ids)
        )

    def add_users(self):
        for i in range(1):
            profile = Profile.objects.create(
                user_name = f.name()
            )
            User.objects.create(
                author_id = profile.id
            )

    def add_tags(self):
        for i in range(10):
            Tag.objects.create(
                name = f.word()
            )

    def add_questions(self, cnt):
        tags_ids = Tag.objects.values_list(
            'id', flat=True
        )
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        for i in range(cnt):
            question = Question.objects.create(
                title=f.sentence()[:128],
                text = '. '.join(f.sentences(f.random_int(min=2, max=5))),
                author_id = choice(users_ids)
            )
            for j in range(f.random_int(min=1, max=5)):
                question.tags.add(choice(tags_ids))

            for j in range(f.random_int(min=1, max=5)):
                self.add_marks(question)


    def fill_questions_with_answers(self, cnt):
        question_ids = Question.objects.values_list(
            'id', flat=True
        )
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        for i in range(cnt):
            answer = Answer.objects.create(
                text = '. '.join(f.sentences(f.random_int(min=2, max=5))),
                question_id = choice(question_ids),
                author_id = choice(users_ids),
            )
            for j in range(f.random_int(min=1, max=5)):
                self.add_marks(answer)





