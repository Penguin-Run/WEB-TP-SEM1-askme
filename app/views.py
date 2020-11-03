from django.shortcuts import render


questions = [
	{
		'id': idx, 
		'title': f'Best question? #{idx}',
		'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the...',
		'tags': [1, 4]
	} for idx in range(7)
]

tags = { 1:'bender', 
         2:'black-jack', 
         3:'perl', 
         4:'MySQL', 
         5:'django',
       }

best_members = {
	1:'Mr.Freeman', 
    2:'Dr.House', 
    3:'Bender', 
    4:'Queen Victoria', 
}


def new_questions(request):
	return render(request, 'index.html', {
        'questions': questions,
        'tags':tags,
        'members':best_members,
    })


def tag_questions(request, string):
	questions_for_this_tag = questions
	return render(request, 'tag_questions.html', {
		'questions': questions_for_this_tag,
	    'tags':tags,
		'tag': string,
		'members':best_members,
		})

def hot_questions(request):
	hot_questions = questions
	return render(request, 'hot_questions.html', {
        'questions': hot_questions,
        'tags':tags,
        'members':best_members,
    })

def ask_question(request):
	return render(request, 'add_question_form.html', {})

def question_answers(request, question_id):
	question = questions[question_id]
	return render(request, 'answers_page.html', {
		'question': question,
		'tags':tags,
		})

def login(request):
	return render(request, 'auth.html', {})

def sign_up(request):
	return render(request, 'registration.html', {})

def settings(request):
	return render(request, 'settings.html', {})
