from django.shortcuts import render


questions = [
	{
		'id': idx, 
		'title': f'title {idx}',
		'text': 'text text',
	} for idx in range(10)
]


# def index(request):
#     return render(request, 'index.html', {
#     	'questions': questions,
#     	})

def index(request):
     return render(request, 'index.html', {})

def hot_questions(request):
	return render(request, 'index.html', {})

def new_questions(request):
	return render(request, 'index.html', {})

def login(request):
	return render(request, 'auth.html', {})

def sign_up(request):
	return render(request, 'registration.html', {})

def settings(request):
	return render(request, 'settings.html', {})

def tag_questions(request):
	return render(request, 'tag_questions.html', {})