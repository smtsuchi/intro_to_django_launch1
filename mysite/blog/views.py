from django.shortcuts import render, redirect

# import models (so we can query from database)
from .models import Post

# import forms (so we can display it in our template)
from .forms import PostForm, UserForm

# import extra functionality: (authentication/login/logout/messages)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    my_posts = [
        {
            'author': 'Shoha Tsuchida',
            'title': "This is my first post!",
            'content': "content1",
            'date_posted': "August 9, 2021"
        },
        {
            'author': 'Ivan Wang',
            'title': "This is Ivan's first post!",
            'content': "content from Ivan",
            'date_posted': "August 9, 2021"
        }
    ]
    context = {'posts': my_posts,}
    # <!-- Syntax for adding python vars: {{ var_goes here }} -->
    # <!-- Syntax for adding python vars: {% expression_goes_here %}
    return render(request, 'blog/index.html', context)

def aboutPage(request):
    return render(request, 'blog/about.html')

def posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'page_title': 'WELCOME TO MY BLOG'
    }
    return render(request, 'blog/posts.html', context)

def createPost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'blog/createpost.html', context)

def registerPage(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'blog/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username") # comes from name attribuet in html input tag
        password = request.POST.get("password1")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f'{user} is logged in!')
            return redirect('blog-index')
    return render(request, 'blog/login.html')

def logoutUser(request):
    logout(request)
    return redirect('blog-login')