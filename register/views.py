from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Extra
from django.contrib.auth.models import User
from .forms import UserRegisterForm ,ExtraForm
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        form2=ExtraForm(request.POST)
        #instantiates the form with the post data

        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            # messages.success(request , username + " , your account has been created")
            # return redirect('/login')   

            if form2.is_valid():
                # form2.save()
                age=form2.cleaned_data.get('age')
                business=form2.cleaned_data.get('business')
                username=form.cleaned_data.get('username')
                user=User.objects.get(username=username)
                print("Helloooo ", user)
                item=Extra(user=user,age=age,business=business)
                item.save()
                messages.success(request , username + " , your account has been created")
                return redirect('/login')
            else:
                return HttpResponse("<h1>Error in form 2</h1>")

        else:
            return HttpResponse("<h1>Error in form 1</h1>")
        # if form.is_valid():
        #     form.save()
        #     username=form.cleaned_data.get('username')
            #form data is stored in a cleaned dictionary 
            
    else:
        form=UserRegisterForm()
        form2=ExtraForm()
    return render(request,'register/register.html',{'form':form,'form2':form2})

@login_required
def profile(request):
    item=Extra.objects.filter(user=request.user)[0]
    age=item.age
    bus=item.business
    return render(request , 'register/profile.html',{'age':age,'bu':bus})