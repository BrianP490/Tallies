"""
URL configuration for Tallies project.

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
from django.conf import settings
from django.conf.urls.static import static  #This function is used to serve static files (like images, stylesheets, or JavaScript) during development.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    # path('/post', include('post.urls')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # adds URL patterns for serving static files during development.

#     When you use static(settings.STATIC_URL, document_root=settings.STATIC_ROOT), Django dynamically generates URL patterns that map requests to URLs under settings.STATIC_URL to static files located in the directory specified by settings.STATIC_ROOT.

#     For example, if STATIC_URL is '/static/' and STATIC_ROOT is 'path/to/your/project/staticfiles/', a request to http://example.com/static/css/style.css will be mapped to the file located at 'path/to/your/project/staticfiles/css/style.css'.