from django.shortcuts import render
from .models import plans

# Create your views here.

def test(request):
    return render(request,"test.html")

def details(request):
    id=request.GET["id"]
    data=plans.objects.get(id=id)
    return render(request,"details.html",{"data":data})

def commentsub(request):
    cmt=request.GET["comment"]
    return render(request,"test.html",{"comments":cmt})