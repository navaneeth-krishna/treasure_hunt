from apps.clues.models import DescQtn
from apps.accounts.models import UserProgress
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render

# Create your views here.

def q1(request):
    user = request.user
    userprogress = user.userprogress
    
    if(request.method == 'POST'):
        userprogress.descq1 = request.POST['q1-ans']
        userprogress.descq1time = timezone.now()
        userprogress.save()
        messages.info(request, "Answer Submitted Successfully")
    
    question = DescQtn.objects.get(q_no=1)
    return render(request, 'descbase.html', {'q1': 'true', 'show': 'true', 'q': question, 'usrprog': userprogress})

def q2(request):
    user = request.user
    userprogress = user.userprogress

    if(request.method == 'POST'):
        userprogress.descq2 = request.POST['q2-ans']
        userprogress.descq2time = timezone.now()
        userprogress.save()
        messages.info(request, "Answer Submitted Successfully")


    question = DescQtn.objects.get(q_no=2)
    return render(request, 'descbase.html', {'q2': 'true',  'show': 'true', 'q': question, 'usrprog': userprogress}) 