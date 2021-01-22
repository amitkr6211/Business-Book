from django.shortcuts import render
from django.contrib.auth.models import User
from .models import MyList2
from .forms import CreateItem
# Create your views here.

def spend(request):
    cur_user=request.user
    if( request.method=="POST"):
        form=CreateItem(request.POST)

        if(form.is_valid()):
            sp=form.cleaned_data["spending"]
            de=form.cleaned_data["description"]

            item=MyList2(user=cur_user,spending=sp,des=de)
            item.save()
    else:
        form=CreateItem()

    my=MyList2.objects.filter(user=cur_user)

    return render(request,'Expenditure/spend.html',{'queryset':my,'form':form})

