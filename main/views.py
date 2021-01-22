from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request,'main/base.html')

def team(request):
    return render(request,'main/team.html')

def about(request):
    return render(request,'main/about.html')