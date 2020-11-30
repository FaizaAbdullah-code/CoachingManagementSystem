from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request,"main.html")
def webpage1(request):
    return render(request,"page1.html")




def nav(request):
    return render(request,"navbar.html")
    
def webpage2(request):
    return render(request,"page2.html")

def webpage3(request):
    return render(request,"studattendence.html")   

def webpage4(request):
    return render(request,"teachattendence.html")   



def webpage5(request):
    return render(request,"teachersprof.html")        


def webpage6(request):
    return render(request,"studentprof.html") 



def webpage7(request):
    return render(request,"studresult.html") 

def webpage8(request):
    return render(request, 'class.html')

def webpage9(request):
    return render(request, 'timetable.html')

def webpage10(request):
    return render(request, 'contact.html')    


def webpage11(request):
    return render(request, 'registration.html' ) 

def webpage12(request):
    return render(request, 'ass.html' ) 

def webpage13(request):
    return render(request, 'schedule.html' ) 





   
