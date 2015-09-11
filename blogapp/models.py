from django.db import models
from django.utils import timezone

# Create your models here.
class Register(models.Model):
	email = models.EmailField(unique=True,max_length=100)
	username = models.CharField(unique=True,max_length=50)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.username

class Profile(models.Model):
	user= models.OneToOneField(Register,unique=True)
	full_name = models.CharField(max_length=100,null=True,blank=True)
	address = models.TextField(null=True,blank=True)
	phone_number = models.CharField(max_length=13,null=True,blank=True)

	def __str__(self):
		return self.full_name

class Post(models.Model):
	#author = models.ForeignKey(user,unique=True)
	author = models.ForeignKey(Register)
	title = models.CharField(max_length=50)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(null=True, blank=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title



