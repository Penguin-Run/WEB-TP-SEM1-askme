from django.core.management.base import BaseCommand, CommandError
from app.models import Question, Answer, User
from random import choice
from faker import Faker

f = Faker()

class Command(BaseCommand):
    help = 'Generates Data'

    def add_arguments(self, parser):
        parser.add_argument('generate_size', type=int)

    def handle(self, *args, **options):
        generate_size = options['generate_size']
        self.fill_questions()

    def fill_questions(self):
        question_ids = Question.objects.values_list(
            'id', flat=True
        )

        users_ids = User.objects.values_list(
            'id', flat=True
        )

        for i in range(3):
                Answer.objects.create(
                text = '. '.join(f.sentences(f.random_int(min=2, max=5))),
                rating = 4,
                question_id = choice(question_ids),
                author_id = choice(users_ids),
            )
