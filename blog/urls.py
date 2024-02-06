"""
URL configuration for puddle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data. 

from django.urls import path

from . import views

app_name = 'blog'                               # IMPORTANT!!! USED to include this file within puddle.settings via app_name

# ITEM url patterns declaration
urlpatterns = [
    path('home/', views.blogs, name='home'),    # This line maps the URL '' to the 'blogs' view function in the ./views.py module. The name 'blogs' can be used to reference this URL in the HTML code (i.e. <form method="get" action="{% url 'item:blogs' %}">)
    
    path('new/', views.new, name='new'),    # This line maps the URL 'new/' to the 'new' view function in the ./views.py module. The name 'new' can be used to reference this URL in the HTML code.

    # path('', views.blog_post, name='Comment'),    # This line maps the URL 'new/' to the 'new' view function in the ./views.py module. The name 'new' can be used to reference this URL in the HTML code.

    path('<int:pk>/', views.detail, name='detail'), #This line captures an integer parameter from the URL and calls the detail function in the ./views.py module. The name 'detail' can be used to reference this URL in the HTML code. 

    path('<int:pk>/delete/', views.delete, name='delete'),  # maps the URL consisting of an integer parameter and the 'delete' path, to the delete function in the views module. The name 'delete' can be used to reference this URL in the HTML code.
    
    path('<int:pk>/edit/', views.edit, name='edit'),  # Captures an integer parameter and maps the URL to the edit function in the views module. The name 'edit' can be used to reference this URL in the HTML code.

    path('explore/', views.explore, name='explore'),  # Matches URL to the explore function in the views module. The name 'explore' can be used to reference this URL in the HTML code.
]