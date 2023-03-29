from django.shortcuts import render,redirect
from .models import plans,comments
from django.http.response import JsonResponse
from django.core.cache import cache

# Create your views here.

def test(request):
    return render(request,"test.html")

def details(request):
    id=request.GET["id"]
    
    if "recent" in request.session:
        if id not in request.session["recent"]:
            request.session["recent"].insert(0,id)

        if len(request.session["recent"])>4:
            request.session["recent"].pop()
        
        print(request.session["recent"])
        obj=plans.objects.filter(id__in=request.session["recent"])
        print(obj)
        request.session.modified=True
    else:
        request.session["recent"]=[id]
        obj=[]

    data=plans.objects.get(id=id)
    
    return render(request,"details.html",{"data":data,"obj":obj})
    
    
def commentsub(request):
    message=request.GET["comment"]
    usr=request.GET["user"]
    id=request.GET["proid"]
    cmt=comments.objects.create(name=usr,msg=message,pro_id=id)
    cmt.save();
    return redirect("/product/?id="+str(id))

def autolist(request):
    if "term" in request.GET:
        name=request.GET["term"]
        print(name)
        data=plans.objects.filter(amount__istartswith=name)
        li=[]
        for i in data:
            li.append(str(i.amount))
        return JsonResponse(li,safe=False)
    
def details2(request):
    id=request.GET["id"]
    if cache.get(id):
        print("DATA FROM CACHE")
        data=cache.get(id)
    else:
        print("DATA FROM DATABASE")
        data=plans.objects.get(id=id)
        cache.set(id,data)
    return render(request,"details.html",{"data":data})
