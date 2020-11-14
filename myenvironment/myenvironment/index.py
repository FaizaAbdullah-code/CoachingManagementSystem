from django.shortcuts import render
from django.http import HttpResponse

def webpage1(request):
    return render(request,"page1.html")

def main(request):
    return render(request,"main.html")



def webpage2(request):
    return render(request,"page2.html")

    