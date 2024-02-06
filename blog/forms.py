from django import forms 

from .models import Blog, BlogComment



INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'    # DECLARE the style for the Blog form

# CREATE a NewBlogForm that includes the Blog's Meta data such as category, name, description, price, image
class NewBlogForm(forms.ModelForm):
    class Meta:         # class for the Blog's Meta Data
        model = Blog
        fields = ('category', 'name', 'content',)

        widgets = { # STYLE THE FIELDS
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'content': forms.Textarea(attrs={
            'class': INPUT_CLASSES
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
    # comment = forms.CharField(widget=forms.Textarea)