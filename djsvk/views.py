from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("<b>welcom to svksvk</b>")

def course(requets):
    return HttpResponse ("PHP,C,PYTHON")

def coursed(requets,courseid):
    return HttpResponse (courseid)

def home(request):
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
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
    