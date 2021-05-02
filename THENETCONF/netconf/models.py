from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from datetime import date, datetime

# Create your models here.
class Partner(models.Model): 
    name = models.CharField(max_length=250) 
    location = models.CharField(max_length=250) 
    picture = models.ImageField(null=True, blank=True,upload_to='images/')

    # category = models.ForeignKey(Category, default="general",on_delete=models.CASCADE)
    # author = models.ForeignKey(User,on_delete=models.CASCADE) 

    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name #name to be shown when called

class Event(models.Model): 
    name = models.CharField(max_length=250) 
    venue = models.CharField(max_length=250)
    Start_date = models.DateField()
    End_date = models.DateField()
    picture = models.ImageField(null=True, blank=True,upload_to='images/')

    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name #name to be shown when called

class CommitteeMember(models.Model): 
    name = models.CharField(max_length=250) 
    role = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    picture = models.ImageField(null=True, blank=True,upload_to='images/')
    
    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name #name to be shown when called

class Participant(models.Model): 

    TYPES = (
        ('Attendee', 'Attendee'),
        ('Presenter', 'Presenter'),
    )
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250, default='Developer')
    email = models.CharField(max_length=250) 
    phone = models.CharField(max_length=250) 
    address = models.CharField(max_length=250)
    presenter = models.CharField(max_length=150, choices=TYPES,default='Attendee')
    topic_to_Present = models.CharField(max_length=250)
    topic_description = models.TextField(max_length=250)
    picture = models.ImageField(null=True, blank=True,upload_to='images/')
    
    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name #name to be shown when called

class Day(models.Model): 
    name = models.CharField(max_length=250) 
    
    def __str__(self):
        return self.name #name to be shown when called

# category = models.ForeignKey(Category, default="general",on_delete=models.CASCADE)

class Program(models.Model): 
    name = models.CharField(max_length=250)
    day = models.ForeignKey(Day,on_delete=models.CASCADE)
    start_time = models.TimeField(default='14:00')
    end_time = models.TimeField(default='15:00')
    speaker = models.ForeignKey(Participant,on_delete=models.CASCADE) 
    description = models.TextField(max_length=250)
    picture = models.ImageField(null=True, blank=True,upload_to='images/')
    
    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name #name to be shown when called

class Contact(models.Model): 
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField(max_length=250) 
    
    def __str__(self):
        return self.name #name to be shown when called
TYPES = (
        ('Attendee', 'Attendee'),
        ('Presenter', 'Presenter'),
    )
