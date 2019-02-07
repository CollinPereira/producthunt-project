from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method== 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'username already exists'})
            except User.DoesNotExist:
                try:
                    user=User.objects.get(email=request.POST['email'])
                    return render(request,'accounts/signup.html',{'error':'email already registered'})                   
                except :
                    user=User.objects.create_user(request.POST['username'],email=request.POST['email'],password=request.POST['password1'])
                    auth.login(request,user)
                    return redirect('home')
           
        else:
            return render(request,'accounts/signup.html',{'error':'passwords did not match'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'incorrect username/password'})
    else:
        return render(request,'accounts/login.html')

    

def logout(request):
    if request.method== 'POST':
        auth.logout(request)
        return redirect('home')