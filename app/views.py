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