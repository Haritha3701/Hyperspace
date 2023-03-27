from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import auth,User
from product.models import plans

# Create your views here.

def samp(request):
    data=plans.objects.all()
    if "user" in request.COOKIES and "price" in request.COOKIES:
        name=request.COOKIES["user"]
        price=request.COOKIES["price"]
        return render(request,"index.html",{"data":data,"name":name,"price":price})
    
    return render(request,"index.html",{"data":data})

def login(request):
    if request.method=="POST":
        
            usr=request.POST["uname"]
            pwd=request.POST["pname"]
            user=auth.authenticate(username=usr,password=pwd)
            if user is not None:
                auth.login(request,user)
                
                msg="login successfully"
                res=redirect("/")
                res.set_cookie("user",usr)
                return res
            else:
                msg="Invalid username and password"
                return render(request,"login.html",{"msg":msg})
    else:
        return render(request,"login.html")

def register(request):
    if request.method=="POST":
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]
        usr=request.POST["uname"]
        email=request.POST["email"]
        pwd=request.POST["pswd"]
        rpwd=request.POST["repswd"]
    
        if pwd==rpwd:
            if User.objects.filter(username=usr).exists():
                msg="Username is already taken"
            elif User.objects.filter(email=email).exists():
                msg="Email is already taken"
            else:
                user=User.objects.create_user(username=usr,first_name=firstname,last_name=lastname,email=email,password=pwd)
                user.save();
                msg="Register successful"
                return redirect("/")

        else:
            msg="Invalid password"
            return render(request,"register.html",{"msg":msg})

    else:                           
        return render(request,"register.html")

    

def logsub(request):
    usr=request.POST["uname"]
    pwd=request.POST["pname"]
    user=auth.authenticate(username=usr,password=pwd)
    if user is not None:
        auth.login(request,user)
        msg="login successfully"
        return redirect("/")
    else:
        msg="Invalid username and password"
        return render(request,"login.html",{"msg":msg})

def regsub(request):
    firstname=request.POST["fname"]
    lastname=request.POST["lname"]
    usr=request.POST["uname"]
    email=request.POST["email"]
    pwd=request.POST["pswd"]
    rpwd=request.POST["repswd"]
    
    if pwd==rpwd:
        if User.objects.filter(username=usr).exists():
            msg="Username is already taken"
        elif User.objects.filter(email=email).exists():
            msg="Email is already taken"
        else:
            user=User.objects.create_user(username=usr,first_name=firstname,last_name=lastname,email=email,password=pwd)
            user.save();
            msg="Register successful"
            return redirect("/")

    else:
        msg="Invalid password"
                               
    return render(request,"register.html",{"msg":msg})

def logout(request):
    auth.logout(request)
    res=redirect("/")
    res.delete_cookie("name")
    res.delete_cookie("user")
    return res

def test(request):
    return render(request,"test.html")
    