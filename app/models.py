from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

class ProfileManager(models.Manager):
	def get_all_users(self):
 		return self.all()

	def get_best_users(self):
 		# TODO: implement logic of best members
 		return self.all()[:15]

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_name = models.CharField(max_length = 256, verbose_name = 'Имя в системе')
	email = models.EmailField(verbose_name = 'E-mail', default = 'default@def.com', blank = True)
	image = models.ImageField(
		upload_to='static/madia/image/avatar/',
		default = 'static/media/image/avatar/200.jpeg',
        blank = True,
        verbose_name='Аватарка'
    ) # TODO: browser can't find image

	objects = ProfileManager()

	def __str__(self):
		return self.user_name

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

# class UserManager(models.Manager):
# 	def get_all_users(self):
# 		return self.all()

# 	def get_best_users(self):
# 		# TODO: implement logic of best members
# 		return self.all()[:15]

# class User(models.Model):
# 	author = models.OneToOneField('Profile', on_delete=models.CASCADE)

# 	objects = UserManager()

# 	def __str__(self):
# 		return self.author.user_name

# 	class Meta:
# 		verbose_name = 'Пользователь'
# 		verbose_name_plural = 'Пользователи'

class MarkManager(models.Manager):
	def count_rating(self):
		return self.filter(mark_type = Mark.MarkType.LIKE).count() - self.filter(mark_type = Mark.MarkType.DISLIKE).count()

class Mark(models.Model):
	class MarkType(models.TextChoices):
		LIKE = 'LIKE', _('Like')
		DISLIKE = 'DIS', _('Dislike')

	mark_type = models.CharField(max_length = 4, choices = MarkType.choices, default = MarkType.LIKE)

	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()

	user = models.ForeignKey('Profile', on_delete = models.CASCADE, verbose_name = 'Автор')

	objects = MarkManager()

	def __str__(self):
		return self.mark_type

	class Meta:
		verbose_name = 'Оценка'
		verbose_name_plural = 'Оценки'
		unique_together = ('content_type', 'object_id', 'user',)

class QuestionManager(models.Manager):
	def new_questions(self):
		return self.all().prefetch_related('author').order_by('-date_create', '-rating')

	def best_questions(self):
		return self.all().prefetch_related('author').order_by('-rating', '-date_create')

	def questions_by_tag(self, tag):
		return self.filter(tags__name = tag)

	def question_by_id(self, question_id):
		return self.get(pk=question_id)

class Question(models.Model):
	title = models.CharField(max_length = 256, verbose_name = 'Заголовок')
	text = models.TextField(verbose_name = 'Текст')
	date_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
	author = models.ForeignKey('Profile', on_delete = models.CASCADE, verbose_name = 'Автор')
	tags = models.ManyToManyField('Tag', verbose_name = 'Тэги')

	# поле должно быть пересчитано при каждом новом добавлении оценки (Mark) этого вопроса
	rating = models.IntegerField(default = 0, blank = True, verbose_name = 'Рейтинг')
	marks = GenericRelation(Mark)
	
	objects = QuestionManager()

	def __str__(self):
		return self.title

	def count_answers(self):
		return Answer.objects.question_answers(self.pk).count()

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'


class AnswerManager(models.Manager):
	def question_answers(self, question_id):
		# return self.filter(question__id = question_id).order_by('-rating', '-date_create')
		return self.filter(question__id = question_id).order_by('-rating', '-date_create')


class Answer(models.Model):
	text = models.TextField(verbose_name = 'Текст')
	date_create = models.DateField(auto_now_add=True, verbose_name = 'Дата создания')
	is_correct = models.BooleanField(default=False, verbose_name = 'Правильность')
	question = models.ForeignKey('Question', on_delete = models.CASCADE, verbose_name = 'Вопрос')
	author = models.ForeignKey('Profile', on_delete = models.CASCADE, verbose_name = 'Автор')

	# поле должно быть пересчитано при каждом новом добавлении оценки (Mark) этого ответа
	rating = models.IntegerField(default = 0, blank = True, verbose_name = 'Рейтинг')
	marks = GenericRelation(Mark)

	objects = AnswerManager()

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'


class TagManager(models.Manager):
	def get_all_tags(self):
		return self.all()

	def get_best_tags(self):
		# TODO: implement logic of best tags
		return self.all()[:25]

class Tag(models.Model):
	name = models.CharField(max_length = 256, unique = True, verbose_name = 'Название тэга')

	objects = TagManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тэг'
		verbose_name_plural = 'Тэги'





