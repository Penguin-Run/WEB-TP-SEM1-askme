from django.shortcuts import render
from django.core.paginator import Paginator


questions = [
	{
		'id': idx, 
		'title': f'Best question? #{idx}',
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
		'tags': [1, 4],
		'likes': 5,
	} for idx in range(9)
]


def new_questions(request, pk = 1):
	question_pages = Paginator(questions, 4)
	# TODO: обработка случая pk > page number

	pages_num = []
	for i in range(1, question_pages.num_pages + 1):
		pages_num.append(i)
	return render(request, 'index.html', {
        'questions': question_pages.page(pk),
        'pages': pages_num
    })


def tag_questions(request, string):
	questions_for_this_tag = questions
	return render(request, 'tag_questions.html', {
		'questions': questions_for_this_tag,
		'tag': string,
		})

def hot_questions(request):
	hot_questions = questions
	return render(request, 'hot_questions.html', {
        'questions': hot_questions,
    })

def ask_question(request):
	return render(request, 'add_question_form.html', {
		})

def question_answers(request, question_id):
	question = questions[question_id]
	return render(request, 'answers_page.html', {
		'question': question,
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
