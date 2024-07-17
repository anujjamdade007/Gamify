from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


# Home page
def home(request):
    return render(request, 'home.html')

# signup page
def user_signup(request):
    page= 'register'
    form = SignupForm()

    #hide the register page for alredy logged users
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = SignupForm(request.POST )
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request , 'user is succesfully created')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request , 'something went wrong')


    context={
        'page':page,
        'form':form,
        }
    return render(request , 'signup.html' , context )


# login page
def user_login(request):
    page= 'signup'
    form = LoginForm()
    #hide the login page for alredy logged users
    if request.user.is_authenticated:
        return redirect('home')
    

    if request.method == 'POST':
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , 'username not found')

        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request ,"User Successfully Logged In")

            return redirect('home')
        else:
            messages.error(request ,"Username or Password not found")
        
    
    context={'page':page,
             'form':form,}
        
    return render(request ,'login.html' , context)



# logout page
def user_logout(request):
    logout(request)
    return redirect('login')