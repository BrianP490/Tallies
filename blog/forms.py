from django import forms 
from .models import Blog, BlogComment



INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'    # DECLARE the style for the Blog form

# CREATE a NewBlogForm that includes the Blog's Meta data such as category, name, description, price, image
class NewBlogForm(forms.ModelForm):
    new_category = forms.CharField(label='Or Create New Category', required=False, max_length=30, widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Optional'
    }))
    
    
    class Meta:         # class for the Blog's Meta Data
        model = Blog
        fields = ('category', 'new_category', 'name', 'content',)

        labels = {  # Define labels for the fields
            'category': 'Select a fitting Category',
            'name': 'Title',  # Specify the label for the 'name' field as 'Title'
        }
        widgets = { # STYLE THE FIELDS
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Blog Title'
            }),
            'content': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter content'
            }),
        }

# Create a Form to Edit a Blog
class EditBlogForm(forms.ModelForm):
    class Meta:         # class for the Blog's Meta Data
        model = Blog
        fields = ('name', 'content',)

        widgets = { # STYLE THE FIELDS
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'content': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:         # class for the Blog's Meta Data
        model = BlogComment     # create an instance of a BlogComent Model
        # fields = ('name', 'content',)
        fields = ('content',)

        widgets = { # STYLE THE FIELDS
            # 'name': forms.TextInput(attrs={
            # 'class': INPUT_CLASSES
            # }),
            'content': forms.Textarea(attrs={
            'placeholder': 'Add A Tallie Comment...',                 # ADD text placeholder   
            'class': INPUT_CLASSES
            }),
        }

