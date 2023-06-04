from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from datetime import datetime
# from .models import loginUser
from django.core.exceptions import ValidationError
import os
from .models import Register, BlogModel
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
# from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    
    blogs = BlogModel.objects.filter(user= request.User)

    return render(request,'index.html',  {'blogs':blogs})

def loginUser(request):

    if request.method == "POST":
        email= request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        print(user,email, password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request,'login.html')

        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        '''    
        user = Register.objects.create(email=email, first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        return redirect('/login')'''
        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")  # Show an error message or handle the situation as desired
            
        try:
            user = Register.objects.create(email=email, first_name=first_name, last_name=last_name, username=username)
            user.set_password(password)
            user.save()
            return redirect('/login')
        except ValidationError as e:
            return HttpResponse(str(e))

    return render(request, 'register.html')

def dashboard(request):
    blog = BlogModel.objects.filter(user= request.user)
    return render(request ,'dashboard/dashboard.html', {'blog':blog})

def blog(request):
    
    blogs = BlogModel.objects.filter(user= request.user)
      
    return render(request ,'blog.html', {'blogs':blogs})

def edit(request, id):
    image = request.FILES.get('image')
    content = request.POST.get('content')
    blog = BlogModel.objects.get(id=id)
    u = BlogModel(image=image, content=content)
    u.save()
    return render(request ,'dashboard/edit.html')

def details(request):

    usr =request.user

    blogs = BlogModel.objects.filter(user= usr)
    return render(request ,'dashboard/detail.html', {'blogs':blogs})

def post(request, id):
    blogs = BlogModel.objects.filter(user= request.user)
    blog = BlogModel.objects.get(id=id)
    blog.save()
    return render(request ,'post.html', {'blog':blog, 'blogs':blogs})

def add(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        if request.method == "POST":
            # print(request.POST.get('username'))
            org_name = request.POST.get('org_name')
            title = request.POST.get('title')
            # slug = slugify(title)
            venue = request.POST.get('venue')
            image = request.FILES.get('image')
            content = request.POST.get('content')
            event_date = request.POST.get('up_dt')

            u = BlogModel( venue=venue, event_date= event_date, org_name= org_name, title=title, user=request.user, image=image, content=content, created_at = datetime.now() )
            u.save()
            
        return render(request ,'dashboard/newpost.html')

def profile(request):

    blogs = BlogModel.objects.filter(user= request.user)
    
    return render(request, "dashboard/profile.html", {'blogs':blogs})

def delete_post(request, id):
    blogs = BlogModel.objects.filter(user= request.user)
    blog = BlogModel.objects.get(id=id)
    blog.delete()
    return redirect('/dashboard', {'blog':blog, 'blogs':blogs})

'''
def profile(request):
    # Retrieve all blog posts from the database
    blog_posts = BlogModel.objects.all()
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})
'''