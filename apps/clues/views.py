from django.shortcuts import render
from .models import Clue
from apps.accounts.models import WonUser, UserProgress
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth.decorators import login_required
import datetime
import os

# Create your views here.
# View to show clue based on the user


def clues(request):

    check_date = datetime.datetime.strptime(os.environ.get("CHECK_DATE"), "%Y, %m, %d, %H, %M, %S")
    deadline_date = datetime.datetime.strptime(os.environ.get("DEADLINE_DATE"), "%Y, %m, %d, %H, %M, %S")
    now = datetime.datetime.now()
    str_check_date = check_date.strftime("%Y-%m-%dT%H:%M:%S")

    if(os.environ.get("TEST_NOW")=='True'):
        now = datetime.datetime.strptime(os.environ.get("NOW"), "%Y, %m, %d, %H, %M, %S")

    show_dash = False
    deadline = False

    user = request.user
    if(user.userprogress.clueReached == 1):
        user.userprogress.updateclue()

    # Setting is dashboard should be shown or not
    if (now >= check_date and now < deadline_date):
        show_dash = True

    # Setting if deadline has been encountered or not
    if(now >= deadline_date):
        deadline = True
    
    print(show_dash)
    print(now)
    print(check_date)

    if(user.userprogress.clueReached < 6):
        clue = Clue.objects.get(clue_no=user.userprogress.clueReached)
        return render(request, 'phase2.html', {'clue': clue, 'show': show_dash, 'deadline': deadline, 'chkdate': str_check_date})

    else:
        user_won = WonUser.objects.get(username=user.username)
        return render(request, 'win.html', {'won': user_won})


# View to check answer
def check(request):

    check_date = datetime.datetime.strptime(os.environ.get("CHECK_DATE"), "%Y, %m, %d, %H, %M, %S")
    deadline_date = datetime.datetime.strptime(os.environ.get("DEADLINE_DATE"), "%Y, %m, %d, %H, %M, %S")
    now = datetime.datetime.now()
    str_check_date = check_date.strftime("%Y-%m-%dT%H:%M:%S")

    if(os.environ.get("TEST_NOW")=='True'):
        now = datetime.datetime.strptime(os.environ.get("NOW"), "%Y, %m, %d, %H, %M, %S")

    show_dash = False
    deadline = False

    user = request.user

    if (now >= check_date and now < deadline_date):
        show_dash = True

    print(show_dash)

    if(now >= deadline_date):
        deadline = True

    if(request.method == 'POST'):
        ans = request.POST['answer']
        no_user = len(WonUser.objects.all())+1

# Checking if the user has won---------------------

        if(user.userprogress.clueReached == 6):
            user_won = WonUser(position=no_user, time_won=timezone.now(), first_name=user.first_name, last_name=user.last_name, username=user.username, email=user.email, clue1Reached=user.userprogress.clue1Reached, clue2Reached=user.userprogress.clue2Reached, clue3Reached=user.userprogress.clue3Reached, clue4Reached=user.userprogress.clue4Reached, clue5Reached=user.userprogress.clue5Reached, clue6Reached=user.userprogress.clue6Reached, clue7Reached=user.userprogress.clue7Reached, clue8Reached=user.userprogress.clue8Reached,
                               clue9Reached=user.userprogress.clue9Reached, clue10Reached=user.userprogress.clue10Reached, clue11Reached=user.userprogress.clue11Reached)
            if(not(WonUser.objects.filter(username=user_won.username).exists())):
                user_won.save()
            won = WonUser.objects.get(username=user.username)
            return render(request, 'win.html', {'user': user, 'won': won})

        else:
            clue = Clue.objects.get(clue_no=user.userprogress.clueReached)
            if(clue.verify(ans)):
                user.userprogress.clueReached += 1
                user.userprogress.updateclue()

# Checking if user has already won---------------------
                if(user.userprogress.clueReached == 6):
                    user_won = WonUser(position=no_user, time_won=timezone.now(), first_name=user.first_name, last_name=user.last_name, username=user.username, email=user.email, clue1Reached=user.userprogress.clue1Reached, clue2Reached=user.userprogress.clue2Reached, clue3Reached=user.userprogress.clue3Reached, clue4Reached=user.userprogress.clue4Reached, clue5Reached=user.userprogress.clue5Reached, clue6Reached=user.userprogress.clue6Reached, clue7Reached=user.userprogress.clue7Reached, clue8Reached=user.userprogress.clue8Reached,
                                       clue9Reached=user.userprogress.clue9Reached, clue10Reached=user.userprogress.clue10Reached, clue11Reached=user.userprogress.clue11Reached)
                    if(not(WonUser.objects.filter(username=user_won.username).exists())):
                        user_won.save()
                    won = WonUser.objects.get(username=user.username)
                    return render(request, 'win.html', {'user': user, 'won': won})

# If user is not won--------------------------
                else:
                    clue = Clue.objects.get(
                        clue_no=user.userprogress.clueReached)
                    return render(request, 'phase2.html', {'clue': clue, 'show': show_dash, 'deadline': deadline, 'chkdate': str_check_date})

            else:
                messages.info(request, "Incorrect Answer! Try again!")
                clue = Clue.objects.get(clue_no=user.userprogress.clueReached)
                return render(request, 'phase2.html', {'clue': clue, 'show': show_dash, 'deadline': deadline, 'chkdate': str_check_date})
