from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from blogapp.models import Register,Profile,Post
from blogapp.forms import RegisterForm,ProfileForm,PostForm,LoginForm

# Create your views here.

def home(request):
    return render(request,'blogapp/base.html',{})

def register(request):
    #A Http Post
    if request.method =='POST' :
        form = RegisterForm(request.POST)

        #Checking the vlaidity of the form
        if form.is_valid():
            #then Save the form
            form.save()
            #Now send the user to home page
            return HttpResponseRedirect('/login/')
        else:
            #the form contains error return  the error
            print (form.errors)

    else:
        #If the request was not a POST method then show the form to enter the details
        form = RegisterForm()

        #Render the form with error if supplied
    return render(request,'blogapp/register.html',{'form':form})

def login(request):
    try:
        if request.session['username']:
            return HttpResponseRedirect('/success/')
    except:
        pass

    if request.method=='POST' :
        form = LoginForm(request.POST)

        if form.is_valid():
            try:
                user = Register.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password'])

                if len(user)==1:
                    request.session['username'] = user[0].username
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
        return render(request,'blogapp/success.html',{})
    else:
        return HttpResponseRedirect('/login/')

def logout(request):    
    del request.session['username']
    return HttpResponseRedirect('/login/')
    

def profile(request):
    if request.session['username']:
        if request.method =="POST" :
            a = Register.objects.get(username=request.session['username'])
            #Finding the column of data of the user logged in
            try :
                b= Profile.objects.get(user=a)
                #Accessing the profile column of the user logged in if the profile exists it loads it 
            except:
                b = Profile(user=a) # A new Profile is creaed if the profile does not exist.
                b.save()
                b= Profile.objects.get(user=a)

            form = ProfileForm(request.POST,instance=b)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login/')
            else:
                return render(request,'blogapp/profile.html',{'form':form})
        else:
            #if the method is not POST
            a=Register.objects.get(username=request.session['username'])

            try:
                b=Profile.objects.get(user=a)
            except:
                b=Profile(user=a)
                b.save()
                b=Profile.objects.get(user=a)

            form = ProfileForm(instance=b)
            return render(request,'blogapp/profile.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')


def profile_view(request):
    if request.session['username']:
        a = Register.objects.get(username=request.session['username'])

        try:
            b=Profile.objects.get(user=a)
        except:
            b=Profile(user=a)
            b.save()
            b=Profile.objects.get(user=a)

        return render(request,'blogapp/profile_view.html',{'profile':b})
    else:
        return HttpResponseRedirect('/login/')
