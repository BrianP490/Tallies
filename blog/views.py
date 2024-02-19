
# blog/views.py

# Create your views here. 
# Views are a mapping of a request to a response. In other words, Views are functions that receive a request and return a response as an output.  Views access the data needed to satisfy requests via models, and delegate(pass the responsibility to another ) the formatting of the response to templates (in this case all HTML files).

# Note: A view can dynamically create an HTML page using an HTML template, populating it with data from a model.


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog, BlogComment, Category
from .forms import NewBlogForm, EditBlogForm, CommentForm
from django.core.paginator import Paginator
Max_Blogs = 2         # Set a total amount of blogs to display on the explore page  
OWNERSHIP = False       # initialize a variable that determines if the current user owns a certain page

# Create your views here.

# BLOGS USER Home VIEW 
# Function: process HTML request of all available blogs
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the blog/Home.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def blogs(request):
    
    blogs = Blog.objects.filter(created_by=request.user.id )  # STORE a list of blogs created by the current user
    # REQUEST is the HTTP request object.
    # 'blog/Home.html' is the template to be rendered that is requested
    # The dictionary {'blogs': blogs} is the context data that will be passed to the template. It includes a key-value pair where the key is 'blogs' and the value is the variable blogs, presumably a list of object blogs.
    return render(request, 'blog/Home.html', {
        'blogs': blogs,  # Return a list of object items
        'OWNERSHIP' : True,
    })


# VISITOR HOME VIEW 
# Function: process HTML request of a user's home page w/ their blogs and profile info
# Parameter(s):
#       request - HttpRequest object
#       pk - the id of the accessed Home page user

# Return Value(s):
#       render function - order the blog/Home.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def ViewProfile(request, pk):

    current_ID = request.user.id                # save the current user's ID
    home_owner = User.objects.filter(id=pk)     # get the id Home page user

    if(current_ID == home_owner[0].id):         # check if the current user owns the home page and is its rightfull owner
        OWNERSHIP = True                        # set flag to true
        blogs = Blog.objects.filter(created_by=request.user.id )  # STORE a list of blogs created by the current user

    else:                               # visitor vistiting another's home page
        OWNERSHIP = False
        blogs = Blog.objects.filter(created_by=pk )  # STORE a list of blogs created by the page's user

    return render(request, 'blog/Home.html', {
        'blogs': blogs,  # Return a list of object items
        'home_owner': home_owner[0],
        'OWNERSHIP': OWNERSHIP,
    })


# EXPLORE PUBLIC BLOGS VIEW
# Function: process HTML request of all available blogs
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the blog/explore.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
@login_required
def explore(request):
    blogs = Blog.objects.exclude(created_by=request.user.id )  # STORE a list of other User's Blogs

    p = Paginator(blogs, Max_Blogs)                             # only allow Max_Blogs number of blog to display
    page = request.GET.get('page') # This line retrieves the value of the 'page' parameter from the GET parameters of the request.
    #The request.GET attribute contains a dictionary-like object that holds all the GET parameters passed in the request URL.
    #request.GET.get('page') attempts to retrieve the value associated with the key 'page'. If the 'page' parameter is present in the URL, it returns its value; otherwise, it returns None.
    blogs_sub_page = p.get_page(page) #This line retrieves a specific page of blog objects from the paginator object p.
    # It calls the get_page() method of the paginator object p and passes the page variable (which contains the page number from the request parameters) as an argument.

    # REQUEST is the HTTP request object.
    # 'blog/explore.html' is the template to be rendered that is requested
    # The dictionary {'blogs_sub_page': blogs_sub_page} is the context data that will be passed to the template. It includes a key-value pair where the key is 'blogs_sub_page' and the value is the variable blogs_sub_pagee, presumably a list of BLOGS.
    return render(request, 'blog/explore.html', {
        'blogs_sub_page': blogs_sub_page,  # Return a list of blogs divided into pages
    })



# BLOG DETAIL VIEW
# Function: process HTML request to show the details of a blog and all of its comments
# Parameter(s):
#       request - HttpRequest object

# Return Value(s):
#       render function - order the blog/detail.html to render on the client's webpage, sending context information to conclude the HTTPResponse object
def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)   # get the Blog with the associating primary key
    comments = BlogComment.objects.filter(Blog=blog)

    # handle a comment submission
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Save the comment to the database or perform other actions
            blogComment = comment_form.save(commit=False)          # CREATE an object for the database ; "commit=False" Wait to commit to the database because an error will occur
            blogComment.created_by = request.user           # AUTHENTICATED by decorator
            blogComment.Blog_id = blog.id                   # AUTHENTICATED by decorator

            request.user.profile.score +=1          # increase the user's profile score
            request.user.profile.save()             # Save the updated profile to the database
            print()


            blogComment.save()                              # SAVE the blog to the database now
            return redirect('blog:detail', pk = blog.id)    # REDIRECT the user to the blog the user created
    else:
        comment_form = CommentForm()


    # REQUEST is the HTTP request object which is sent.
    # 'blog/detail.html' is the template to be rendered that is requested
    # The dictionary {'blogs': blogs, 'comment_form': comment_form, 'blog': blog } is the context data that will be passed to the template. It includes a key-value pair where the key is 'blogs' and the value is the variable blogs 
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

            new_category = form.cleaned_data['new_category']        # extract the name of the new category, if any
            category_instance = None                # initialize this variable

            if new_category:  # If a new category name is provided
                category_instance, _ = Category.objects.get_or_create(name=new_category) # create the new Category
                blog.category = category_instance       # assign the newly created category as a blog attribute

            blog.created_by = request.user          # save the blog's creator
            request.user.profile.score +=1          # increase the user's profile score

            request.user.profile.save()             # Save the updated profile to the database
            blog.save()                             # SAVE the blog to the database now

            return redirect('blog:detail', pk = blog.id)    # REDIRECT the user to the blog the user created
    else:                                            #GET REQUEST or elsewise
        form = NewBlogForm()                         # CREATE a null blog form

    # CALL blog/form.html to render with the form and title as context info
    return render(request, 'blog/form.html', {
        'form': form,
        'title': 'New blog',
    })



# EDIT BLOG VIEW
# Function: process HTML request to edit an blog
# Parameter(s):
#       request - HttpRequest object
#       pk - the blog's unique ID
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
# Function: process HTML request to delete an blog 
# Parameter(s):
#       request - HttpRequest object
#       pk - on blog's unique private ID

# Return Value(s):
#       redirect function - order a redirect to the blog:home URL
@login_required
def delete(request, pk):
    item = get_object_or_404(Blog, pk=pk, created_by=request.user)  # GET the blog 
    item.delete()                                           # DELETE the blog from the database
    return redirect('blog:home')                      # REDIRECT to dashboard index