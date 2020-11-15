from django.shortcuts import render
from django.core.paginator import Paginator
import random
from app.models import Question
from app.models import Answer

NUMBER_OF_QUESTIONS = 27

tags = { 1:'bender', 
		2:'black-jack', 
		3:'perl', 
		4:'MySQL', 
		5:'django',
	}

sample_question_answers = [
	{
		'id': idx,
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
	} for idx in range(7)
]

questions = [
	{
		'id': idx, 
		'title': f'Best question? #{idx}',
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
		# выбирает случайный тэг из dict tags. !!! dict tags дублируется здесь и в context processors!! TODO: исправить
		# явялется числом хотя должен формировать массив. TODO:Исправить!!
		'tags': random.choice(list(range(1, 6))), 
		'likes': 5,
		'answers': sample_question_answers,
	} for idx in range(NUMBER_OF_QUESTIONS)
]

def paginate(request, object_list, per_page=3):
    paginator = Paginator(object_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def new_questions(request):
	new_questions = Question.objects.new_questions()
	question_pages = paginate(request, new_questions)

	return render(request, 'index.html', {
        'page_obj': question_pages,
    })

def hot_questions(request):
	hot_questions = Question.objects.best_questions()
	question_pages = paginate(request, hot_questions)

	return render(request, 'hot_questions.html', {
        'page_obj': question_pages,
    })

def tag_questions(request, tag):
	questions_for_this_tag = Question.objects.questions_by_tag(tag)
	page_obj = paginate(request, questions_for_this_tag)

	return render(request, 'tag_questions.html', {
        'page_obj': page_obj,
        'tag': tag,
    })

def question_answers(request, question_id):
	question = questions[question_id]
	question_answers = Answer.objects.question_answers(question_id)

	page_obj = paginate(request, question_answers)
	return render(request, 'answers_page.html', {
		'page_obj': page_obj,
		'question': question,
		})

def ask_question(request):
	return render(request, 'add_question_form.html', {
		})

def login(request):
	return render(request, 'auth.html', {
		})

def sign_up(request):
	return render(request, 'registration.html', {
		})

def settings(request):
	return render(request, 'settings.html', {
		})
