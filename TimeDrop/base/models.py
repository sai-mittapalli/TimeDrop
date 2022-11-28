from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Event(models.Model):
    # host = 
    # topic = 

    eventName = models.CharField(max_length=200)
    dueDate = models.DateField()
    eventTime = models.TimeField()
    eventDescription = models.TextField(blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #calendarModel = models.ForeignKey(CalendarSave, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventName

class CalendarSave(models.Model):
    calendarName = models.CharField(max_length=50)
    #calendarColor = models.CharField(max_length=10)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.calendarName

#class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  firstName = models.CharField(max_length=100, blank=True)
   # lastName = models.CharField(max_length=100, blank=True)
    #email = models.EmailField(max_length=150)
    
    #def __str__(self):
     #   return self.user.username

#@receiver(post_save, sender=User)
#def updateProfileSignal(sender, instance, created, **kwargs):
 #   try:
  #      instance.profile.save()
   # except ObjectDoesNotExist:
    #    Profile.objects.create(user=instance)
