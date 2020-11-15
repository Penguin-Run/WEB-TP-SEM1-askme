from app.models import Tag, User

def tags(arg):
	tags = Tag.objects.get_all_tags()
	return { 'tags': tags }

def best_members(arg):
	best_members = User.objects.get_all_users()
	return { 'members': best_members }