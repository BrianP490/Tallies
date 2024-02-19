#core/forms.py

# HTML Forms are used to collect user data for processing on the server. Django simplifies form creation, validation, and processing
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile



# Create a class used to store login information using the user form for authentication, provided by Django ; class derived from AuthenticationForm
class LoginForm(AuthenticationForm):
    #By default, these fields are required ; message will appear if left empty ; to make optional add "required=False"
    # since required, when the user does not enter information, a message to input pops up
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))



#Form used to create a new profile (each user will have a Profile; 1 to 1 relationship)
class RegisterProfileForm(forms.ModelForm): # access the profile attributes
    #By default, these fields are required ; message will appear if left empty ; to make optional add "required=False"
    # since required, when the user does not enter an age, a message to enter an age pops up
    age = forms.IntegerField(label='Age', help_text='Enter your age', required=True, widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your age',                # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))  # Create an IntegerField for age  # Label is Just a title that can be rendered ; EX. {{ form.username.label_tag }}
    
    # since required, when the user does not upload a profile pic, a message to select one pops up
    profile_image = forms.ImageField(label='Profile Image', required=False, widget=forms.FileInput(attrs={

        'accept': 'image/*',                             # Hide the default file input
    }))

    class Meta:                             # Attributes
        model = Profile                     # base the model off of the Profile class
        fields = ('age', 'profile_image')   # MAKE THESE fields available on the form



# Form used during User Registration ; derived from UserCreationForm class
class RegisterUserForm(UserCreationForm):

    class Meta:                     # RegisterUserForm class attribute
        model = User                # Meta model attribute
        fields = ( 'username', 'first_name', 'email', 'password1', 'password2')                # Meta fields attribute
        # Note: all User fields:
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    # Select the form field to manipulate and pull data input from
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'placeholder': 'Your First Name',               # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    email = forms.CharField(required=False, label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-enter your password',        # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    }))

    # watch out when copying and pasting    
    def __init__(self, *args, **kwargs):                        # INITIALIZES USER'S SUPER CONSTRUCTOR USING INFORMATION FROM THE FORM DATA
        super(RegisterUserForm, self).__init__(*args, **kwargs) #calls the constructor of the parent (UserCreationForm class)




# START OF UPDATE USER/PROFILE SECTION 
class UpdUserForm(forms.ModelForm):
    username = forms.CharField(label='Change Username', widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',                 # ADD text placeholder
        'class': 'w-full py-4 px-6 rounded-xl'          # ADD styling to the fields
    })) # Label is Just a title that can be rendered ; EX. {{ form.username.label_tag }}
    class Meta:
        model = User
        #modify fields to show relevant information
        # fields = ('username', 'first_name', 'last_name', 'email', 'password') #old
        fields = ('username',) # modified from above ; allow modification of these fields 

 

#USED FOR UPDATE USER/PROFILE SECTION
class UpdProfileForm(forms.ModelForm): # access the profile attributes
    class Meta:
        model = Profile     # base the model off of the Profile class
        fields = ('profile_image',)   # allow modification of these fields 

    widgets = {                             # STYLE THE FIELDS           
        'profile_image': forms.FileInput(attrs={'id': 'profileImageInput'}),        # ASSIGN THE FILE THAT IS SUBMITTED AN IDENTIFIER
    }
