from apps.clues.models import DescQtn
from apps.accounts.models import UserProgress
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render
import datetime
import os

# Create your views here.

def q1(request):
    user = request.user
    userprogress = user.userprogress

    check_date = datetime.datetime.strptime(os.environ.get("CHECK_DATE"), "%Y, %m, %d, %H, %M, %S")
    deadline_date = datetime.datetime.strptime(os.environ.get("DEADLINE_DATE"), "%Y, %m, %d, %H, %M, %S")
    now = datetime.datetime.now()
    str_check_date = check_date.strftime("%Y-%m-%dT%H:%M:%S")

    if(os.environ.get("TEST_NOW")=='True'):
        now = datetime.datetime.strptime(os.environ.get("NOW"), "%Y, %m, %d, %H, %M, %S")

    show_dash = False
    deadline = False

    if (now >= check_date and now < deadline_date):
        show_dash = True

    # Setting if deadline has been encountered or not
    if(now >= deadline_date):
        deadline = True
    
    if(request.method == 'POST'):
        userprogress.descq1 = request.POST['q1-ans']
        userprogress.descq1time = timezone.now()
        userprogress.save()
        messages.info(request, "Answer Submitted Successfully")
    
    question = DescQtn.objects.get(q_no=1)
    return render(request, 'descbase.html', {'q1': 'true', 'show': show_dash, 'deadline': deadline,'q': question, 'usrprog': userprogress, 'chkdate': str_check_date})

def q2(request):
    user = request.user
    userprogress = user.userprogress

    check_date = datetime.datetime.strptime(os.environ.get("CHECK_DATE"), "%Y, %m, %d, %H, %M, %S")
    deadline_date = datetime.datetime.strptime(os.environ.get("DEADLINE_DATE"), "%Y, %m, %d, %H, %M, %S")
    now = datetime.datetime.now()
    str_check_date = check_date.strftime("%Y-%m-%dT%H:%M:%S")

    if(os.environ.get("TEST_NOW")=='True'):
        now = datetime.datetime.strptime(os.environ.get("NOW"), "%Y, %m, %d, %H, %M, %S")

    show_dash = False
    deadline = False

    if (now >= check_date and now < deadline_date):
        show_dash = True

    # Setting if deadline has been encountered or not
    if(now >= deadline_date):
        deadline = True

    if(request.method == 'POST'):
        userprogress.descq2 = request.POST['q2-ans']
        userprogress.descq2time = timezone.now()
        userprogress.save()
        messages.info(request, "Answer Submitted Successfully")


    question = DescQtn.objects.get(q_no=2)
    return render(request, 'descbase.html', {'q2': 'true',  'show': show_dash, 'deadline': deadline,  'q': question, 'usrprog': userprogress, 'chkdate': str_check_date}) 