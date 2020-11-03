from django.shortcuts import render


questions = [
	{
		'id': idx, 
		'title': f'Best question? #{idx}',
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
	} for idx in range(7)
]

tags = { 'tag_1':'bender', 
         'tag_2':'black-jack', 
         'tag_3':'perl', 
         'tag_4':'MySQL', 
         'tag_5':'django',
       }



def new_questions(request):
	return render(request, 'index.html', {
        'questions': questions,
        'tags':tags,
    })

def hot_questions(request):
	return render(request, 'index.html', {})

def ask_question(request):
	return render(request, 'add_question_form.html', {})

def question_answers(request, question_id):
	question = questions[question_id]
	return render(request, 'answers_page.html', {
		'question': question
		})

# TEMP!!!!
def answers(request):
	return render(request, 'answers_page.html', {
		'tags':tags
		})

def login(request):
	return render(request, 'auth.html', {})

def sign_up(request):
	return render(request, 'registration.html', {})

def settings(request):
	return render(request, 'settings.html', {})

def tag_questions(request, string):
	return render(request, 'tag_questions.html', {
		'questions': questions,
        'tags':tags,
		'tag': string,
		})