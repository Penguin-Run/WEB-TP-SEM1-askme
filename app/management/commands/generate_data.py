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
        parser.add_argument(
            '--db_size',
            choices=['test', 'small', 'medium', 'large'],
            help='choose how many data to generate'
        )
        parser.add_argument('--add_users', type=int, help='users creation')
        parser.add_argument('--add_tags', type=int, help='tags creation')
        parser.add_argument('--add_questions', type=int, help='questions creation')
        parser.add_argument('--add_answers', type=int, help='answers creation')
        # parser.add_argument('--add_marks', type=int, help='marks creation')

    def handle(self, *args, **options):
        opt = options['db_size']
        if (opt):
            part = {
                'test': 0.0001,
                'small': 0.0005,
                'medium': 0.001,
                'large': 0.01,
                }.get(opt, 0.00005)
            self.generate_database(part)

        if (options['add_users']):
            self.generate_users(options['add_users'])
        if (options['add_tags']):
            self.generate_tags(options['add_tags'])
        if (options['add_questions']):
            self.generate_questions(options['add_questions'])
        if (options['add_answers']):
            self.fill_questions_with_answers(options['add_answers'], [])
        # if (options['add_marks']):
        #     self.generate_marks(options['add_marks'])

    def generate_database(self, part):
        MAX_USER = 10000
        MAX_QUESTION = 50000
        MAX_TAG = 10000
        MAX_ANSWER = 100000
        MAX_MARKS = 200000

        if (part > 1):
            return;

        self.generate_users(int(MAX_USER * part))
        self.generate_tags(int(MAX_TAG * part))
        self.generate_questions(int(MAX_QUESTION * part))


    def generate_marks(self, mark_object):
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        enum = [Mark.MarkType.LIKE, Mark.MarkType.DISLIKE]
        mark = Mark.objects.create(
            mark_type = choice(enum),
            content_object = mark_object,
            user_id = choice(users_ids)
        )

    def generate_users(self, cnt):
        for i in range(cnt):
            profile = Profile.objects.create(
                user_name = f.name()
            )
            User.objects.create(
                author_id = profile.id
            )

    def generate_tags(self, cnt):
        for i in range(cnt):
            Tag.objects.create(
                name = f.word()
            )

    def generate_questions(self, cnt):
        tags_ids = Tag.objects.values_list(
            'id', flat=True
        )
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        added_questions_ids = []
        for i in range(cnt):
            question = Question.objects.create(
                title=f.sentence()[:128],
                text = '. '.join(f.sentences(f.random_int(min=2, max=5))),
                author_id = choice(users_ids)
            )
            added_questions_ids.append(question.id)
            for j in range(f.random_int(min=1, max=5)):
                question.tags.add(choice(tags_ids))

            for j in range(f.random_int(min=1, max=5)):
                self.generate_marks(question)

        self.fill_questions_with_answers(cnt*2, added_questions_ids)



    def fill_questions_with_answers(self, cnt, question_ids):
        if(len(question_ids) == 0):
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
                self.generate_marks(answer)





