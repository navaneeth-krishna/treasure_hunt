from django.contrib import admin
from .models import UserProfile, WonUser, UserProgress
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserProgress)
admin.site.register(WonUser)
