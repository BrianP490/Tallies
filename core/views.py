from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegisterUserForm, RegisterProfileForm, UpdUserForm, UpdProfileForm
from .models import Profile
from django.db import transaction
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def home(request):
#     return render(request, 'core/index.html', {})


# REGISTER VIEW
# Function: process HTML request containing 2 registration form 
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the core/Register.html to render on the client's webpage, sending the user's form information to conclude the HTTPResponse object
@transaction.atomic # makes sure both forms save to the database correctly
def Register(request):
    if request.method =='POST':         # CHECK if the user triggered a post request

        # print(request)

        form = RegisterUserForm(request.POST)  # Pass request.FILES to handle file uploads & STORE the rest of the new USER's data from the signup form data

        profile_form = RegisterProfileForm(request.POST or None, request.FILES) # create a profile form object from the submitted Form

        if form.is_valid() and profile_form.is_valid():             # CHECK if both forms are valid
            user = form.save()# save user form data into a user object ; also because of the signaling, this command creates a profile that is linked to the user 

            # Check if a profile already exists for the user
            profile, created = Profile.objects.get_or_create(user=user)

            # Update the profile if it already exists
            if not created:
                profile_form = RegisterProfileForm(request.POST, request.FILES, instance=profile)

            # Save the profile form data
            profile_form.save()

            # username = form.cleaned_data['username'] #retrieves the cleaned value of the username field of the SignUpForm
            # password = form.cleaned_data['password1']#retrieves the cleaned value of the password1 field of the SignUpForm   

            # # Log user in usin credentials
            # user = authenticate(username=username, password=password)
            # login(request,user)  #sets the user in the session

            return redirect('/')  # REDIRECT the user to the login page after valid registration
        else:   # future error handling here
            print(form.is_valid()) 
            print(profile_form.is_valid())          


    else:  # This handles all other requests (GET, etc)
        form = RegisterUserForm() # create a brand new user registration form 
        profile_form = RegisterProfileForm() # create a brand new profile registration form

    # RENDER the request on the core/signup.html with context data from the form
    return render(request, 'core/Register.html', {
    'form':form, "p_form": profile_form                         # USE the form as a data argument   
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

@login_required
@transaction.atomic # makes sure both forms save to the database correctly
def Update(request):
    if request.method == "POST":
        #get info from both forms (UpdUserForm&UpdProfileForm) & existing user/profile data. you are telling Django to create a form instance based on the data from the POST request, but also populate it with the data from the request.user instance. 
        user_form = UpdUserForm(request.POST or None, request.FILES or None, instance=request.user)

        user_profile_form = UpdProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)  # since profile is associated with user in a 1 to 1 relation. Profile can be accessed from user 
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save() # save user form data  
            user_profile_form.save() # save userProfile data
            return redirect('blog:home') # return to profile page
    else:  # GET requests senario & populate existing user/profile data
        # PASS 2 FORMS ONTO THE PAGE    
        user_form = UpdUserForm(instance=request.user)
        
        user_profile_form = UpdProfileForm(instance=request.user.profile)  # since profile is associated with user in a 1 to 1 relation. Profile can be accessed from user 

    return render(request, 'core/Update.html', {'u_form':user_form, 'p_form': user_profile_form})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User                              
    success_url = reverse_lazy('core:login')  # Redirect to core's login page after user is deleted
    template_name = 'core/Unregister.html'

    def get_object(self, queryset=None):        # Not necessary to define in this case
        return self.request.user  