from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

class Profile(models.Model):
	user_name = models.CharField(max_length = 256, verbose_name = 'Имя в системе')
	email = models.EmailField(verbose_name = 'E-mail')
	# поле для хранения аватарки ImageField ?

	def __str__(self):
		return self.user_name

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

class User(models.Model):
	author = models.OneToOneField('Profile', on_delete=models.CASCADE)

	def __str__(self):
		return self.author.user_name

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Mark(models.Model):
	class MarkType(models.TextChoices):
		LIKE = 'LIKE', _('Like')
		DISLIKE = 'DIS', _('Dislike')

	mark_type = models.CharField(max_length = 4, choices = MarkType.choices, default = MarkType.LIKE)

	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()

	user = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Автор')


class QuestionManager(models.Manager):
	def new_questions(self):
		return self.order_by('-date_create', '-rating')

	def best_questions(self):
		return self.order_by('-rating', '-date_create')

	def questions_by_tag(self, tag):
		return self.filter(tags__name = tag)

class Question(models.Model):
	title = models.CharField(max_length = 256, verbose_name = 'Заголовок')
	text = models.TextField(verbose_name = 'Текст')
	date_create = models.DateField(auto_now_add=True, verbose_name = 'Дата создания')
	rating = models.IntegerField(verbose_name = 'Рейтинг')
	author = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Автор')
	tags = models.ManyToManyField('Tag', verbose_name = 'Тэги')

	marks = GenericRelation(Mark)
	
	objects = QuestionManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'


class AnswerManager(models.Manager):
	def question_answers(self, question_id):
		return self.filter(question__id = question_id).order_by('-rating', '-date_create')


class Answer(models.Model):
	text = models.TextField(verbose_name = 'Текст')
	rating = models.IntegerField(verbose_name = 'Рейтинг')
	date_create = models.DateField(auto_now_add=True, verbose_name = 'Дата создания')
	is_correct = models.BooleanField(default=False, verbose_name = 'Правильность')
	question = models.ForeignKey('Question', on_delete = models.CASCADE, verbose_name = 'Вопрос')
	author = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Автор')

	marks = GenericRelation(Mark)

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





