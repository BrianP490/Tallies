from django.contrib import admin
from .models import Blog, Category, BlogComment


# Register your models here to the django database

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(BlogComment)