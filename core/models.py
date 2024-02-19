from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create a Profile class that is linked to a user. This profile will store additional content that the default user class does not store
class Profile(models.Model):
    #DEFAULT FIELDS:
    user = models.OneToOneField(User, on_delete=models.CASCADE) # connect the user the the profile using the user PK(id)
    
    #CUSTOM FIELDS:
    # follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    
    age = models.IntegerField(null=True, blank=True)  # Allow null and blank values for flexibility

    profile_image = models.ImageField(null=True, default='DEFAULT.png', blank=True, upload_to="profile_images/") # optional ; saves image media location ; # NEED TO INSTALL PILLOW (Python Image Library) ; sets default image to media/DEFAULT.png
    score = models.IntegerField(null=True, blank=True, default=0)  # Allow null and blank values for flexibility

    # date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username
    
#create profile AUTOMATICALLY when new user signs up using signals
#try decorator: @receiver (post_save, sender=User)
    # signals allow processes to know when something happens
    #triggered when post gets saved reveiver 
@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
# capture post saves from the user table