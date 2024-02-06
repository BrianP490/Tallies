
# blog/views.py

# Create your views here. 
# Views are a mapping of a request to a response. In other words, Views are functions that receive a request and return a response as an output.  Views access the data needed to satisfy requests via models, and delegate(pass the responsibility to another ) the formatting of the response to templates (in this case all HTML files).

# Note: A view can dynamically create an HTML page using an HTML template, populating it with data from a model.


from django.contrib.auth.decorators import login_required
from django.db.models import Q              # USED to search for terms within the description of each item object
from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog, BlogComment
from .forms import NewBlogForm, EditBlogForm, CommentForm


# Create your views here.

# BLOGS VIEW 
# Function: process HTML request of all available blogs
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the blog/blogs.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def blogs(request):
    
    blogs = Blog.objects.filter(created_by=request.user.id )  # STORE a list of unsold item objects

    # REQUEST is the HTTP request object.
    # 'item/blogs.html' is the template to be rendered that is requested
    # The dictionary {'blogs': blogs} is the context data that will be passed to the template. It includes a key-value pair where the key is 'blogs' and the value is the variable blogs, presumably a list of object blogs.
    return render(request, 'blog/Home.html', {
        'blogs': blogs,  # Return a list of object items
        # 'userName': request.user.name,
    })

# EXPLORE VIEW
# Function: process HTML request of all available blogs
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the blog/explore.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def explore(request):
    
    blogs = Blog.objects.exclude(created_by=request.user.id )  # STORE a list of other User's Blogs

    # REQUEST is the HTTP request object.
    # 'item/explore.html' is the template to be rendered that is requested
    # The dictionary {'explore': explore} is the context data that will be passed to the template. It includes a key-value pair where the key is 'explore' and the value is the variable explore, presumably a list of object explore.
    return render(request, 'blog/explore.html', {
        'blogs': blogs,  # Return a list of object items
    })

# DETAIL VIEW
# Function: process HTML request to show a user's blog and all of its comments
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the item/detail.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)   # get the Blog with the associating primary key
    comments = BlogComment.objects.filter(Blog=blog)


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Save the comment to the database or perform other actions
            blogComment = comment_form.save(commit=False)          # CREATE an object for the database ; "commit=False" Wait to commit to the database because an error will occur
            blogComment.created_by = request.user          # AUTHENTICATED by decorator
            blogComment.Blog_id = blog.id          # AUTHENTICATED by decorator

            blogComment.save()                             # SAVE the blog to the database now
            return redirect('blog:detail', pk = blog.id)    # REDIRECT the user to the blog the user created
    else:
        comment_form = CommentForm()

    # related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]  # store 3 related items of the same category

    # REQUEST is the HTTP request object which is sent.
    # 'blog/detail.html' is the template to be rendered that is requested
    # The dictionary {'blogs': blogs, 'related_blogs': related_blogs } is the context data that will be passed to the template. It includes a key-value pair where the key is 'blogs' and the value is the variable blogs 
    return render(request, 'blog/detail.html', {
        'comments': comments,
        'comment_form': comment_form,
        'blog': blog,

    })

# NEW BLOG VIEW
# Function: process HTML request to create a new blog
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order a redirect to view the created blog if the user's form is valid or order the blog/form.html to re-render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def new(request):
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES) # CALL NewBlogForm to execute using the data submitted within a field form and any files submitted 

        if form.is_valid():                         # CHECK if the form is valid
            blog = form.save(commit=False)          # CREATE an object for the database ; "commit=False" Wait to commit to the database because an error will occur
            blog.created_by = request.user          # AUTHENTICATED by decorator
            blog.save()                             # SAVE the blog to the database now

            return redirect('blog:detail', pk = blog.id)    # REDIRECT the user to the blog the user created
    else:
        form = NewBlogForm()            # CREATE a null blog form

    # CALL blog/form.html to render with the form and title as context info
    return render(request, 'blog/form.html', {
        'form': form,
        'title': 'New blog',
    })

# NEW BLOG COMMENT POST VIEW
# Function: process HTML request to create a new blog comment
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order a redirect to view the created blog if the user's form is valid or order the blog/form.html to re-render on the client's webpage, sending context information to conclude the HTTPResponse object

# def blog_post(request, blog_id):

#     blog = get_object_or_404(Blog, pk=blog_id)   # get the Blog with the associating primary key

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             # Save the comment to the database or perform other actions
#             blogComment = comment_form.save(commit=False)          # CREATE an object for the database ; "commit=False" Wait to commit to the database because an error will occur
#             blogComment.created_by = request.user          # AUTHENTICATED by decorator
#             blogComment.save()                             # SAVE the blog to the database now

#             return redirect('blog:home')
#             # return redirect('blog:detail.html', pk = blog_id)    # REDIRECT the user to the blog the user commented on
#             # return redirect('blog:post_detail', post_id=post_id)
#     else:
#         comment_form = CommentForm()

#     return render(request, 'blog:detail.html', { 'blog': blog, 'comment_form': comment_form, })






# EDIT BLOG VIEW
# Function: process HTML request to edit an item
# Parameter(s):
#       request - HttpRequest object
#       pd - the blog's unique ID
# Return Value(s):
#       render function - order a redirect to view the created blog if the user's form is valid or order the blog/form.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk, created_by=request.user)  # GET the blog 

    if request.method == 'POST':
        form = EditBlogForm(request.POST, request.FILES, instance=blog) # create an edit blog form using the data from the submitted form, any files sent in, and associates the form with a specific instance of your model (a blog instance) which allows the form to be pre-filled with the current data of the blog being edited.

        if form.is_valid():                         # CHECK if the form is valid
            form.save()                             # SAVE the blog's info to the Django database

            return redirect('blog:detail', pk = blog.id)    # REDIRECT the user to the blog detail page
    form = EditBlogForm(instance=blog)      # discard any changes made during the edit and reinitialize the form 

    # CALL blog/form.html to render with the form and title as context info
    return render(request, 'blog/form.html', {
        'form': form,
        'title': 'Edit blog',
    })

# DELETE VIEW
# Function: process HTML request to delete an item
# Parameter(s):
#       request - HttpRequest object
#       pk - on item's unique private key

# Return Value(s):
#       redirect function - order a redirect to the dashboard/index URL
@login_required
def delete(request, pk):
    item = get_object_or_404(Blog, pk=pk, created_by=request.user)  # GET the item 
    item.delete()                                           # DELETE the item from the database
    return redirect('blog:home')                      # REDIRECT to dashboard index