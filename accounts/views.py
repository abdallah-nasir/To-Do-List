from django.shortcuts import render,redirect,reverse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse("frontend:list"))
    form=UserRegister(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data["username"]
        password=form.cleaned_data["password"]
        User.objects.create_user(username=username,password=password)
        user=authenticate(request,username=username,password=password)
        login(request,user)
        return redirect(reverse("frontend:list"))
    context={"form":form}
    return render(request,"signup.html",context)

def signin(request):
    if request.user.is_authenticated:
        return redirect(reverse("frontend:list"))
    form=UserLogin(request.POST or None)
    if form.is_valid():
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse("frontend:list"))
        else:
            messages.error(request,"username/password is not correct")

    context={"form":form}
    return render(request,"signin.html",context)


def signout(request):
    logout(request)
    return redirect(reverse("accounts:signin"))
   

  

    