from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import UserProfile, UserProgress

# Create your views here.

# View to handle login requests


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("User Authenticated")

            # for usr in User.objects.all():
            #     UserProgress.objects.get_or_create(user=usr)
            #     UserProfile.objects.get_or_create(user=usr)

            auth.login(request, user)
            return redirect('/dashboard/guidelines')
        else:
            messages.info(request, "Invalid Username and Password")
            return redirect('login')

    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# View to handle user registrations
def register(request):

    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2 or User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
            else:
                messages.info(request, "Passwords not Matching")
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name) #, last_name=last_name)
            user.save()

        return redirect('/')
    else:
        return render(request, 'register.html')


# View to handle profile updations
def editprofile(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        profile.user_contact = request.POST['user_contact']
        profile.teammate_name1 = request.POST['teammate_name1']
        profile.teammate_name2 = request.POST['teammate_name2']
        profile.teammate_name3 = request.POST['teammate_name3']
        profile.teammate_name4 = request.POST['teammate_name4']
        profile.teammate_name5 = request.POST['teammate_name5']
        profile.save()
        messages.info(request, "Profile Saved Successfully")

    return render(request, 'profile.html', {'prof': profile})
