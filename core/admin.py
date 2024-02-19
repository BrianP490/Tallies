
#extend User model
 #https://www.youtube.com/watch?v=KNvSWubOaQY&list=PLCC34OHNcOtoQCR6K4RgBWNi3-7yGgg7b&index=2

from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


# Register your models here to the django database


#mix profile and user models ; Note:must be defined before UserAdmin class
class ProfileInline(admin.StackedInline):
    model = Profile
    # use all attributes of the Profile Model. This includes ['follows', 'age', 'score', 'profile_image]


# Build the UserAdmin class from the ModelAdmin base class
# Override the UserAdmin
class UserAdmin(admin.ModelAdmin):

    model = User    # focus on the User model 
    #display a subset of the Django User fields on admin page
    fields = [
        'username', 'first_name', 'last_name', 'email'
    ]

    # change the add view to remove the profile settings 
    def add_view(self, *args, **kwargs):
        self.inlines=[] # remove the profile info fields from this section
        return super(UserAdmin, self).add_view(*args,**kwargs) # use the existing add view from the parent class
    
    # modify the change view to show the profile settings 
    def change_view(self, *args, **kwargs):
        self.inlines=[ProfileInline] # show the profile info fields
        return super(UserAdmin, self).change_view(*args,**kwargs) # use the existing add view from the parent class


admin.site.unregister(User) # unregister the default django user model from admin page

admin.site.register(User, UserAdmin) # registers the User model with the Django admin interface using the UserAdmin class as the custom admin options.