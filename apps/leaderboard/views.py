from django.shortcuts import render
from apps.accounts.models import UserProgress
# from django.contrib.auth.decorators import login_required
import datetime
import os

# Create your views here.
def leaderboard(request):

    lead = UserProgress.objects.raw('''SELECT * FROM accounts_userprogress WHERE accounts_userprogress."user_id" NOT IN(1,2,3) ORDER BY  accounts_userprogress."clueReached" DESC,accounts_userprogress."lastClueReached" ASC''')[:10]
    
    now = datetime.datetime.now()
    check_date = datetime.datetime.strptime(os.environ.get("CHECK_DATE"),"%Y, %m, %d, %H, %M, %S")

    show_dash = False
    str_check_date = check_date.strftime("%Y-%m-%dT%H:%M:%S")

    if (now >= check_date) :
        show_dash=True

    return render(request,'leaderboard.html',{'leads':lead,'show':show_dash, 'chkdate':str_check_date})