from django.shortcuts import render, redirect

# import models (so we can query from database)
from .models import Post

# import forms (so we can display it in our template)
from .forms import PostForm, UserForm

# import extra functionality: (authentication/login/logout/messages)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# import mail dependecies
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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

@login_required(login_url='blog-login')
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

        user = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")

        context = {"username": user}

        template = render_to_string('blog/emailtemplate.html', context)

        email_message = EmailMessage(
            'Welcome to my Django Blog!', #Subject Line
            template, # body
            settings.EMAIL_HOST_USER,
            [email],
        )

        email_message.fail_silently = False
        email_message.send()

        messages.success(request, "Account was created for " + user)

        return redirect('blog-login')

    context = {'form': form}
    return render(request, 'blog/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username") # comes from name attribute in html input tag
        password = request.POST.get("password1")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f'{user} is logged in!')
            return redirect('blog-index')
        messages.info(request, "Incorrect username OR password")
    return render(request, 'blog/login.html')

@login_required(login_url='blog-login')
def logoutUser(request):
    logout(request)
    return redirect('blog-login')

def individualPost(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {'p':post}
    return render(request, 'blog/individualpost.html', context)

@login_required(login_url='blog-login')
def updatePost(request, post_id):
    post =Post.objects.get(id=post_id)
    print(request.user.is_superuser)
    if post.author.id != request.user.id:
            messages.info(request, "You cannot update another user's post!")
            return redirect('blog-posts')
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully updated your post")
        return redirect('blog-individualpost', post_id=post_id)

    context = {'form': form}
    return render(request, 'blog/updatepost.html', context)

@login_required(login_url='blog-login')
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author.id != request.user.id:
        messages.info(request, "You cannot delete another user's post!")
        return redirect('blog-posts')
    post.delete()
    messages.success(request, "The post was successfully deleted")
    return redirect('blog-posts')