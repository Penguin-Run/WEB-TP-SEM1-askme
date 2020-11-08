from django.shortcuts import render
from django.core.paginator import Paginator

sample_question_answers = [
	{
		'id': idx,
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
	} for idx in range(9)
]

questions = [
	{
		'id': idx, 
		'title': f'Best question? #{idx}',
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
		'tags': [1, 4],
		'likes': 5,
		'answers': sample_question_answers,
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

def hot_questions(request, pk = 1):
	hot_questions = questions
	question_pages = Paginator(hot_questions, 4)
	# TODO: обработка случая pk > page number

	pages_num = []
	for i in range(1, question_pages.num_pages + 1):
		pages_num.append(i)
	return render(request, 'hot_questions.html', {
        'questions': question_pages.page(pk),
        'pages': pages_num
    })

def tag_questions(request, string, pk = 1):
	questions_for_this_tag = questions
	question_pages = Paginator(questions_for_this_tag, 4)
	# TODO: обработка случая pk > page number

	pages_num = []
	for i in range(1, question_pages.num_pages + 1):
		pages_num.append(i)
	return render(request, 'tag_questions.html', {
        'questions': question_pages.page(pk),
        'pages': pages_num,
        'tag': string,
    })

def question_answers(request, question_id, pk = 1):
	question = questions[question_id]

	answers_pages = Paginator(question['answers'], 4)

	pages_num = []
	for i in range(1, answers_pages.num_pages + 1):
		pages_num.append(i)
	return render(request, 'answers_page.html', {
		'question': question,
		'answers_pages': answers_pages.page(pk),
		'pages': pages_num,
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
