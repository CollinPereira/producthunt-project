from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request,'products/home.html')

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            pro=product()
            pro.title=request.POST['title']
            pro.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                pro.url= request.POST['url']
            else:
                pro.url="http://"+request.POST['url'] 
            pro.image=request.FILES['image']
            pro.icon=request.FILES['icon']
            pro.pub_date=timezone.datetime.now()
            pro.hunter=request.user
            pro.save()
            return redirect('home')
        else:
            return render(request,'productscreate.html',{'error':'enter all the fields'})
    else:
        return render(request,'products/create.html')
