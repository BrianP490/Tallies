#core/forms.py

# HTML Forms are used to collect user data for processing on the server. Django simplifies form creation, validation, and processing
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create a class used to store login information using the user form for authentication, provided by Django ; class derived from AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))

# Class that is used to store form information for user input ; derived from UserCreationForm class
class SignupForm(UserCreationForm):
    class Meta:                     # SignupForm class attribute
        model = User                # Meta model attribute
        fields = ('username', 'email', 'password1', 'password2')                # Meta fields attribute


    # Select the form field to manipulate and pull data input from
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-enter your password',        # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))