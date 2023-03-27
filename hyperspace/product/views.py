from django.shortcuts import render,redirect
from .models import plans,comments


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