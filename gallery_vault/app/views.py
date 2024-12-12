from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def user_login(req):
    if 'user' in req.session:
        return redirect(index)
    else:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            print(data)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname     #create
                    return redirect(index)
                else:
                    req.session['user']=uname
                    return redirect(index)
            else:
                messages.warning(req,'invalid username or password')
                return redirect(user_login)            
        return render(req,'login.html')



# def user_login(req):
#     if req.method=='POST':
#         uname=req.POST.get("uname")
#         password=req.POST.get("password")
#         user=authenticate(req,username=uname,password=password)
#         if user:
#             login(req,user)
#             if user.is_superuser:
#                 req.session['shop']=uname
#                 return redirect(index)
#             else:
#                 req.session['user']=uname
#                 return redirect(index)
#         else:
#             messages.warning(req, "Invalid Username or Password")
#             return redirect(login)
#     else:
#         return render(req,'login.html')


def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
        except:
            messages.warning(req,'user details already exists')
            return redirect(register)
        return redirect(login)
    else:
        return render(req,'register.html')
    


def index(req):
    if 'user' in req.session:
        data=UploadedFile.objects.all()
        return render(req,'index.html',{'file':data})
    else:
        return redirect(login)