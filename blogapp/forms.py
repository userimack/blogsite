from django import forms
from blogapp.models import Register,Profile,Post

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Register
		fields = ['email','username','password']

class ProfileForm(forms.Modelform):
	class Meta:
		model = Profile
		fields =['full_name','address','phone_number']

class LoginForm(forms.ModelForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','text']
		


