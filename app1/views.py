from django.shortcuts import render
from django.http import HttpResponse
from app1 import views


def index(request):
    return HttpResponse("<h1>welcome to index page1</h1>")

def sample1(request):
    return render(request,"appp1/sample1.html")


def sample_app1(request):
    return render(request,"sample_app1.html")


def carry_data(request,data):
    return HttpResponse(f'<h1>The Recieved data is {data}</h1>')

def facto(request,num):
    fact=1
    for i in range(int(num),1,-1):
        fact*=i
    return HttpResponse(f'<h2>the factorial of {num} is {fact}</h2>')


def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(num1+num2)
# Create your views here.
