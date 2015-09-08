from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from blogapp.models import Register,Profile,Post

# Create your views here.

def home(request):
	return HttpResponse(request,'blogapp/base.html')

def register(request):
	#A Http Post
	if request.method =='POST' :
		form - ProfileForm(request.POST)

		#Checking the vlaidity of the form
		if form.is_valid():
			#then Save the form
			form.save()
			#Now send the user to home page
			return HttpResponeRedirect('//')
		else:
			#the form contains error return  the error
			return (form.errors)

	else:
		#If the request was not a POST method then show the form to enter the details
		form = RegisterForm()

		#Render the form with error if supplied
		return render(request,'blogapp/register.html',{'form':form})
def login(request):
	try:
		if request.session['username']:
			return HttpResponeRedirect('/success/')
	except:
		pass

	if request.method=='POST' :
		form = LoginForm(request.POST)

		if form.is_valid():
			try:
				user = Register.objects.filter(username = form.cleaned_data['username'],password= form.cleaned_data['password'])

				if len(user)==1:
					request.session=user[0].username;
					return HttpResponseRedirect('/success/')
				else:
					return HttpResponse("Log In Credential's didn't match!! Please Try Again ")
			except DoesNotExit:
				return None
		else:
			form = LoginForm()
			return render(request,'blogapp/login.html',{'form':form})

def success(request):
	if request.session['username']:
		return render(request,'blogapp/success.html')
	else:
		return HttpResponseRedirect('/login/')

def logout(request):
	if request.session['username']:
		del request.session['username']
		return HttpResponseRedirect('/login/')
	else:
		return HttpResponseRedirect('/login/')