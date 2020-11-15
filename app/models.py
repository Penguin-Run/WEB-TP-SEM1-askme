from django.db import models


class User(models.Model):
	user_name = models.CharField(max_length = 256, verbose_name = 'Имя в системе')
	email = models.EmailField(verbose_name = 'E-mail')
	# поле для хранения аватарки ImageField ?
	# поле для хранения пароля ??

	def __str__(self):
		return self.user_name

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

class QuestionManager(models.Manager):
	def new_questions(self):
		return self.order_by('-date_create', '-rating')

	def best_questions(self):
		return self.order_by('-rating', '-date_create')

class Question(models.Model):
	title = models.CharField(max_length = 256, verbose_name = 'Заголовок')
	text = models.TextField(verbose_name = 'Текст')
	date_create = models.DateField(auto_now_add=True, verbose_name = 'Дата создания')
	rating = models.IntegerField(verbose_name = 'Рейтинг')
	author = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Автор')
	tags = models.ManyToManyField('Tag', verbose_name = 'Тэги')
	
	objects = QuestionManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'


class AnswerManager(models.Manager):
	def answers_by_date(self):
		return self.order_by('-date_create', '-rating')

	def best_answers(self):
		return self.order_by('-rating', '-date_create')


class Answer(models.Model):
	text = models.TextField(verbose_name = 'Текст')
	rating = models.IntegerField(verbose_name = 'Рейтинг')
	date_create = models.DateField(auto_now_add=True, verbose_name = 'Дата создания')
	is_correct = models.BooleanField(default=False, verbose_name = 'Правильность')
	question = models.ForeignKey('Question', on_delete = models.CASCADE, verbose_name = 'Вопрос')
	author = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Автор')

	objects = AnswerManager()

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'


class Tag(models.Model):
	name = models.CharField(max_length = 256, verbose_name = 'Название тэга')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тэг'
		verbose_name_plural = 'Тэги'


