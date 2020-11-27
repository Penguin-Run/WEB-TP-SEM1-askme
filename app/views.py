from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
import random

from app.models import Question
from app.models import Answer

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app.forms import LoginForm, AskForm


def paginate(request, object_list, per_page = 5):
    paginator = Paginator(object_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def new_questions(request):
	# sample how to use data in session, sessions will be very handy for hw-4
	print(f'HELLO: { request.session.get("hello") }')

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
	question = Question.objects.question_by_id(question_id)
	question_answers = Answer.objects.question_answers(question_id)

	page_obj = paginate(request, question_answers)
	return render(request, 'answers_page.html', {
		'page_obj': page_obj,
		'question': question,
		})

@login_required
def ask_question(request):
	if request.method == 'GET':
		form = AskForm() # TODO: doesn't redirect back on ask form after logging in
	else:
		form = AskForm(data=request.POST)
		if form.is_valid():
			question = form.save(commit = False)
			question.author = request.user.profile
			question.save()
			return redirect(reverse('question_answers', kwargs = {'question_id': question.pk}))

	ctx = { 'form': form }
	return render(request, 'add_question_form.html', ctx)

def login(request):
	if request.method == 'GET':
		form = LoginForm()
	else:
		form = LoginForm(data=request.POST)
		if form.is_valid():
			user = auth.authenticate(request, **form.cleaned_data)
			if user is not None:
				# sample how to store data in sessions
				request.session['hello'] = 'world'

				auth.login(request, user)
				# /?next = /polls/3
				return redirect("/") # TODO: сделать адаптивный редирект, чтобы возвращал туда откуда пришли на аутентифию
	ctx = { 'form': form }
	return render(request, 'auth.html', ctx)

def logout(request):
	auth.logout(request)
	return redirect("/")

def sign_up(request):
	return render(request, 'registration.html', {
		})

def settings(request):
	return render(request, 'settings.html', {
		})
