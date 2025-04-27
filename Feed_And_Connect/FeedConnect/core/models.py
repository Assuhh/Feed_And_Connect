from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.utils.timezone import now


User = get_user_model()

# Create your models here.

class FeedingSchedule(models.Model):
    pet_name = models.CharField(max_length=100)
    feeding_time = models.TimeField()
    portion_size = models.FloatField()  

class FeedingLog(models.Model):
    pet_name = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(default=now)
    portion_dispensed = models.FloatField(default=0.0)  
    success = models.BooleanField(default=True)
   
    
class FeedHistory(models.Model):
    FEED_TYPE_CHOICES = (
        ('manual' , 'Manual'),
        ('scheduled', 'Scheduled'),
    )
    
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(help_text= " Amount of Food Dispensed")
    feed_type = models.CharField(max_length=10, choices= FEED_TYPE_CHOICES)
    
    def _str_(self):
           return f"{self.timestamp} - {self.feed_type} - {self.amount}"
        
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture-973460_1280.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
