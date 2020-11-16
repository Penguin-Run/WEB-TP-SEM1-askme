from django.core.management.base import BaseCommand, CommandError
from app.models import Question, Answer, User, Tag
from random import choice
from faker import Faker

f = Faker()

class Command(BaseCommand):
    help = 'Generates Data'

    def add_arguments(self, parser):
        parser.add_argument('generate_size', type=int)

    def handle(self, *args, **options):
        generate_size = options['generate_size']
        self.add_questions()
        self.fill_questions()

    def add_questions(self):
        tags_ids = Tag.objects.values_list(
            'id', flat=True
        )
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        for i in range(5):
            question = Question.objects.create(
                title=f.sentence()[:128],
                text = '. '.join(f.sentences(f.random_int(min=2, max=5))),
                author_id = choice(users_ids)
            )
            for j in range(f.random_int(min=1, max=5)):
                question.tags.add(choice(tags_ids))


    def fill_questions(self):
        question_ids = Question.objects.values_list(
            'id', flat=True
        )
        users_ids = User.objects.values_list(
            'id', flat=True
        )

        for i in range(5):
            Answer.objects.create(
                text = '. '.join(f.sentences(f.random_int(min=2, max=5))),
                question_id = choice(question_ids),
                author_id = choice(users_ids),
            )
