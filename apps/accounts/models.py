
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_contact = models.CharField(
        max_length=15, blank='True', null='True', default=" ")
    teammate_name1 = models.CharField(
        max_length=50, blank='True', null='True', default=" ")
    teammate_name2 = models.CharField(
        max_length=50, blank='True', null='True', default=" ")
    teammate_name3 = models.CharField(
        max_length=50, blank='True', null='True', default=" ")
    teammate_name4 = models.CharField(
        max_length=50, blank='True', null='True', default=" ")
    teammate_name5 = models.CharField(
        max_length=50, blank='True', null='True', default=" ")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_userprofile_and_clues(sender, instance, created, **kwargs):
    if created:
        UserProgress.objects.create(user=instance)
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile_and_clues(sender, instance, **kwargs):
    instance.userprogress.save()
    instance.userprofile.save()

# Model to keep track of time when the user reaches a particular clue


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clueReached = models.IntegerField(default=1)
    lastClueReached = models.DateTimeField(null=True, blank=True)
    clue1Reached = models.DateTimeField(null=True, blank=True)
    clue2Reached = models.DateTimeField(null=True, blank=True)
    clue3Reached = models.DateTimeField(null=True, blank=True)
    clue4Reached = models.DateTimeField(null=True, blank=True)
    clue5Reached = models.DateTimeField(null=True, blank=True)
    clue6Reached = models.DateTimeField(null=True, blank=True)
    clue7Reached = models.DateTimeField(null=True, blank=True)
    clue8Reached = models.DateTimeField(null=True, blank=True)
    clue9Reached = models.DateTimeField(null=True, blank=True)
    clue10Reached = models.DateTimeField(null=True, blank=True)
    clue11Reached = models.DateTimeField(null=True, blank=True)
    clue12Reached = models.DateTimeField(null=True, blank=True)
    clue13Reached = models.DateTimeField(null=True, blank=True)
    clue14Reached = models.DateTimeField(null=True, blank=True)
    clue15Reached = models.DateTimeField(null=True, blank=True)
    clue16Reached = models.DateTimeField(null=True, blank=True)
    #Model fields specific for Stem-ed
    descq1time = models.DateTimeField(null=True, blank=True)
    descq1 = models.TextField(null=True, blank=True)
    descq2time = models.DateTimeField(null=True, blank=True)
    descq2 = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.user.username

    def updateclue(self):
        self.lastClueReached = timezone.now()
        if(self.clueReached == 1):
            self.clue1Reached = timezone.now()
        elif(self.clueReached == 2):
            self.clue2Reached = timezone.now()
        elif(self.clueReached == 3):
            self.clue3Reached = timezone.now()
        elif(self.clueReached == 4):
            self.clue4Reached = timezone.now()
        elif(self.clueReached == 5):
            self.clue5Reached = timezone.now()
        elif(self.clueReached == 6):
            self.clue6Reached = timezone.now()
        elif(self.clueReached == 7):
            self.clue7Reached = timezone.now()
        elif(self.clueReached == 8):
            self.clue8Reached = timezone.now()
        elif(self.clueReached == 9):
            self.clue9Reached = timezone.now()
        elif(self.clueReached == 10):
            self.clue10Reached = timezone.now()
        elif(self.clueReached == 11):
            self.clue11Reached = timezone.now()
        elif(self.clueReached == 12):
            self.clue11Reached = timezone.now()
        elif(self.clueReached == 13):
            self.clue11Reached = timezone.now()
        elif(self.clueReached == 14):
            self.clue11Reached = timezone.now()
        elif(self.clueReached == 15):
            self.clue11Reached = timezone.now()
        elif(self.clueReached == 16):
            self.clue11Reached = timezone.now()
        super(UserProgress, self).save()


# Model to keep record of all the users who completed all the questions
class WonUser(models.Model):
    position = models.IntegerField(default=0)
    time_won = models.DateTimeField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    clue1Reached = models.DateTimeField(null='True')
    clue2Reached = models.DateTimeField(null='True')
    clue3Reached = models.DateTimeField(null='True')
    clue4Reached = models.DateTimeField(null='True')
    clue5Reached = models.DateTimeField(null='True')
    clue6Reached = models.DateTimeField(null='True')
    clue7Reached = models.DateTimeField(null='True')
    clue8Reached = models.DateTimeField(null='True')
    clue9Reached = models.DateTimeField(null='True')
    clue10Reached = models.DateTimeField(null='True')
    clue11Reached = models.DateTimeField(null='True')
    clue12Reached = models.DateTimeField(null='True')
    clue13Reached = models.DateTimeField(null='True')
    clue14Reached = models.DateTimeField(null='True')
    clue15Reached = models.DateTimeField(null='True')
    clue16Reached = models.DateTimeField(null='True')