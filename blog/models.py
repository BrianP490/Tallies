from django.contrib.auth.models import User         # import django User model
from django.db import models                        # import django models class

# Create your models here.

# Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database

# Stored data includes the field types and possibly also their maximum size, default values, selection list options, help text for documentation, label text for forms, etc. 



# CREATE a Class structure for Category added to the database ; subclass of the models Model class
class Category(models.Model):
    name = models.CharField(max_length=255) # create a max length restriction

    class Meta:                     # CREATE a Meta data class
        ordering = ('name',)                    # Order all category entries within django admin in alphabetical order
        verbose_name_plural = 'Categories'      # Show the title 'Categories' instead of default 'Categorys' within admin site's sidebar

    def __str__(self):              # FUNCTION that returns the Category name
        return self.name

# CREATE a Class to contain all the Blog Messages
class Blog(models.Model):
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE)        # related_name='blogs': This provides a reverse relation from "Category" back to the model where this line of code is located. It means that you can access the instances of the current model associated with a Category using the attribute name blogs. For example, if you have a Category instance, you can access its associated blogs using category.blogs.all().
    # ALSO, "on_delete=models.CASCADE" : when a user is deleted the item is also deleted
    name = models.CharField(max_length=255) # create a max length restriction of the Blog Name ; name is used in the admin page
    members = models.ManyToManyField(User, related_name='Blogs')           # involves the owner and the contacter
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE,blank=True, null=True)   
    # This provides a reverse relation from User back to the model where this line of code is located. It means that you can access the instances of the current model associated with a User using the attribute name blogs. For example, if you have a User instance, you can access the blogs created by that user using user.blogs.all().
    # "on_delete=models.CASCADE" : when a user is deleted the item is also deleted
    created_at = models.DateTimeField(auto_now_add=True)                            # store the time the Blog instanciated
    modified_at = models.DateTimeField(auto_now=True)                               # update to the current time

    class Meta:
        ordering = ('-modified_at',)
    def __str__(self):              # FUNCTION that returns the Category name
        return self.name

# CREATE the Blog Comment class that will be contained within Blog
    # not using message due to crashing with Django
class BlogComment(models.Model):
    Blog = models.ForeignKey(Blog, related_name='Comments', on_delete=models.CASCADE)   # This line of code is creating a ForeignKey relationship between the current model and the Blog model, and it establishes a reverse relation named 'Comments' from Blog back to the current model. Refers back to the Blog that this comment is associated with
    content = models.TextField(blank=True, null=False) # blank=True: This means that the field is allowed to be empty when a form is submitted. ; null=False: This means that in the database, the field cannot store a NULL value.
    created_at = models.DateTimeField(auto_now_add=True)                            # store the time the Blog instanciated
    created_by = models.ForeignKey(User, related_name='Created_Comments', on_delete=models.CASCADE) # creating a ForeignKey relationship between the current model and the User model, and it establishes a reverse relation named 'created_Comments' from User back to the current model. The CASCADE option ensures that when the User is deleted, the associated instances of the current models are also deleted.

    class Meta:
        ordering = ('created_at',) # the results are in oldest to newest configuration 
        
        # (-created_at) the results will be ordered from the newest to the oldest based on the created_at field. 5 4 3 2 1

    def __str__(self):              # FUNCTION that returns the commenter and the time the comment was created
        formatted_created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S') # display a formatted version of the created_at field in your __str__ method without the microseconds, you can use the strftime method available
        return f'{self.created_by} - {formatted_created_at}'
