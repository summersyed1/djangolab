from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"homepage.html")

def index1(request):
    return render(request,"projects.html")

def index2(request):
    return render(request,"contact.html")

def index3(request):
    return render(request,"cv.html")