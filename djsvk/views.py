from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import usersform
from sousvk.models import svk


def aboutus(request):
    return HttpResponse("<b>welcom to svksvk</b>")

def course(requets):
    return HttpResponse ("PHP,C,PYTHON")

def coursed(requets,courseid):
    return HttpResponse (courseid)

def home(request):
    
    svkdata=svk.objects.all()
    # for a in svkdata:
    #     print(a.icon)
    
    data={
        'svkdata':svkdata
        
    }
    
    
    # data={
    #     'title':'Home NEW',
    #     'bdata':"WELCOME BABY",
    #     'clist':['PHP','JAVA','DJANGO'],
    #     'numbers':[1,2,3,4,5,6],
    #     'student_details':[
    #         {'name':'John Doe','age':25,'city':'New York'},
    #         {'name':'Emily Johnson','age':18,'city':'London'},
    #     ]
    # }
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")

def userform(request):
    final='blank'
    fn=usersform()
    data={'form':fn}
    
    try:
        if request.method=='POST':
        # email=request.GET["email"]
        # passw=request.GET["passw"]
        # city=request.GET["city"]
        # addr=request.GET["addr"]
        # zip=request.GET["zip"]
    
        # email=request.GET.get("email")
        # passw = request.GET.get('passw')
        # city=request.GET.get("city")
        # addr=request.GET.get("addr")
        # zip=request.GET.get("zip")  
            email=request.POST.get("email")
            passw = request.POST.get('passw')
            city=request.POST.get("city")
            addr=request.POST.get("addr")
            zip=request.POST.get("zip")      
        
            final=f'Email is {email},Password is {passw}'
            # data={
            #     'email':email,
            #     'passw':passw,
            #     'city':city,
            #     'addr':addr,
            #     'zip':zip,
            #     'output':final
            # }
            data={
                'form':fn,
                'output':final
            }
            url=f"/aboutus/?n={data['output']}"
            #return HttpResponseRedirect('/aboutus/')
            return  HttpResponseRedirect (url)
        
    except:
        pass
        
    return render(request,"userform.html",data) 


def subm(request):
    return HttpResponse(request)
    