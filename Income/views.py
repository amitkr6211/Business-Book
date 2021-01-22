from django.shortcuts import render,HttpResponse
from .models import MyList
from Expenditure.models import MyList2
from .forms import CreateItem,Calculate
from django.contrib.auth.decorators import login_required
# Create your views here.
def bep_q(fc,vc,sp,ass):
    ans =fc/(sp-vc)
    return (round(ans,2))

def bep_s(fc,vc,sp,ass):
    ans =(fc/(sp-vc))*sp
    return (round(ans,2))

def contribution(fc,vc,sp,ass):
    ans = sp-vc
    return (round(ans,2))

def moss(fc,vc,sp,ass):
    ans = ass-bep_s(fc,vc,sp,ass)
    return (round(ans,2))

def calculate(request):
    bepq=0
    beps=0
    cont=0
    mos=0
    if request.method=="POST":
        form=Calculate(request.POST)
        if form.is_valid():
            fc=form.cleaned_data["fixed_cost"]
            vc=form.cleaned_data["variable_cost"]
            sp=form.cleaned_data["selling_price"]
            ass=form.cleaned_data["actual_sales"]
            bepq=bep_q(fc,vc,sp,ass)
            beps=bep_s(fc,vc,sp,ass)
            cont=contribution(fc,vc,sp,ass)
            mos=moss(fc,vc,sp,ass)
        else:
            return HttpResponse('<h1>Error in form validation</h1>')
    else:
        form=Calculate()
    return render(request , 'Income/compute.html',{'form':form,'bepq':bepq,'beps':beps,'cont':cont,'mos':mos})

@login_required
def choice(request):
    return render(request , 'Income/choice.html')

@login_required
def profit(request):
    cur_user=request.user
    my1=MyList.objects.filter(user=cur_user)
    my2=MyList2.objects.filter(user=cur_user)
    total_profit=0
    total_spending=0
    
    for item in my1:
        total_profit+=item.income

    for item in my2:
        total_spending+=item.spending

    net_profit=total_profit-total_spending
    return render(request,'Income/profit.html',{'profit':total_profit,'spend':total_spending,'net':net_profit})

@login_required
def income(request):
    cur_user=request.user
    if request.method=="POST":
        form=CreateItem(request.POST)
        if form.is_valid():
            inc=form.cleaned_data["income"]
            de=form.cleaned_data["description"]
            it=MyList(user=cur_user,income=inc,des=de)
            it.save()
    else:
        form=CreateItem()
    my=MyList.objects.filter(user=cur_user)
    return render(request,'Income/income.html',{'queryset':my,'form':form})

def info(request):
    return render(request,'Income/info.html')