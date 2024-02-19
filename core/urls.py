from django.contrib.auth import views as auth_views     #use the provided authentication views for tasks such as logging in, logging out, resetting passwords, etc.
from django.urls import path
from . import views
from .forms import LoginForm
from .views import UserDeleteView

app_name = 'core'                               # IMPORTANT!!!!! USED to include this file within puddle.settings via app_name


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),       
    # Root Directory ; Sends user to the login page

    #Match the argument route (pattern: 'login/' ) and call the as_view() function within the imported auth_view using "core/login.html" as the template to render;  The name='login' parameter provides a way to reference this specific URL pattern in your Django project (ex. within template HTML files).
    # all the possible as_view arguments: 
    #auth_views.LoginView.as_view(
    #     template_name='myapp/login.html',
    #     authentication_form=CustomAuthenticationForm,
    #     extra_context={'key': 'value'},
    #     redirect_authenticated_user=True
    # ),

    path('Register/', views.Register, name='Register'),  # Match the argument route (pattern: 'Register/' ) and call the Register function; user will be Directed to the Register.html page
    
    path('Unregister/', UserDeleteView.as_view(), name='Unregister'), #We use the as_view() method to convert the UserDeleteView class-based view into a callable view for use in URL patterns. We give the URL pattern a name of 'Unregister' which can be used to reference it in Django templates or elsewhere in the code.

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),       # Match the argument route (pattern: 'logout/' ) and call the as_view() function within the imported auth_view; user will be logged out of their account and will be redirected to the URL defined by LOGOUT_REDIRECT_URL within settings.py

    path('About/', views.About, name='About'),  # Match the argument route (pattern: 'About/' ) and call the About() function within the imported auth_view; user will be Directed to the About.html page
    
    path('Privacy/', views.Privacy, name='Privacy'),  # Match the argument route (pattern: 'Privacy/' ) and call the Privacy() function within the imported auth_view; user will be Directed to the Privacy.html page

    path('LoadTTT/', views.LoadTTT, name='TTT'),  # Match the argument route (pattern: 'LoadTTT/' ) and call the LoadTTT() function within the imported auth_view; user will be Directed to the TTT.html page

    path('Contact/', views.Contact, name='Contact'),  # Match the argument route (pattern: 'Contact/' ) and call the Contact() function within the imported auth_view; user will be Directed to the Contact.html page

    path('Terms/', views.Terms, name='Terms'),  # Match the argument route (pattern: 'Terms/' ) and call the Terms() function within the imported auth_view; user will be Directed to the Terms.html page

    path('Update/', views.Update, name='Update'),  # Match the argument route (pattern: 'Update/' ) and call the Update function within the imported views file; user will be Directed to the core/Update.html page
]