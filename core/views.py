from django.shortcuts import render, redirect
from .forms import SignupForm
# Create your views here.

# def home(request):
#     return render(request, 'core/index.html', {})


# SIGNUP VIEW
# Function: process HTML request containing a signup form 
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the core/signup.html to render on the client's webpage, sending the user's form information to conclude the HTTPResponse object
def SignUp(request):
    if request.method =='POST':         # CHECK if the user triggered a post request
        form = SignupForm(request.POST) # STORE the new user's data from the signup form data

        if form.is_valid():             # CHECK if the form is valid
            form.save()                 # SAVE the user to the django database

            return redirect('/login/')  # REDIRECT the user to the login page after valid form submittion
    else:
        form = SignupForm()             # CREATE an empty signup form 

    # RENDER the request on the core/signup.html with context data from the form
    return render(request, 'core/signup.html', {
    'form':form                         # USE the form as a data argument   
    })


def login(request):
    return render(request,'core/login.html', {})

def About(request):
    return render(request,'core/About.html', {})

def Privacy(request):
    return render(request,'core/Privacy.html', {})

def LoadTTT(request):
    return render(request,'core/TTT.html', {})

def Contact(request):
    return render(request,'core/Contact.html', {})

def Terms(request):
    return render(request,'core/Terms.html', {})