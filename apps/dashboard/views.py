from django.shortcuts import render
# Create your views here.

# Serving Guidelines on Login


def guidelines(request):

    user = request.user
    return render(request, 'dashboard.html')
