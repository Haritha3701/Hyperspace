from django.shortcuts import render,redirect
from .models import plans,comments


# Create your views here.

def test(request):
    return render(request,"test.html")

def details(request):
    id=request.GET["id"]
    data=plans.objects.get(id=id)
    return render(request,"details.html",{"data":data})

def commentsub(request):
    message=request.GET["comment"]
    usr=request.GET["user"]
    id=request.GET["proid"]
    cmt=comments.objects.create(name=usr,msg=message,pro_id=id)
    cmt.save();
    return redirect("/product/?id="+str(id))