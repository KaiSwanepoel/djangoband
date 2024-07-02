from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post


def signup(request):
    """This function renders the signup page

    Parameters:
        request: HttpRequest object

    Returns:
        HttpResponse object
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('band:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})


def user_login(request):
    """This function renders the login page

    Parameters:
        request: HttpRequest object

    Returns:
        HttpResponse object
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect(reverse('band:home'))
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


def user_logout(request):
    """This function renders the logout page

    Parameters:
        request: HttpRequest object
        
    Returns:
        HttpResponse object
    """
    logout(request)
    return redirect(reverse('band:index'))


def index(request):
    """
    This function renders the landing page
    """
    return render(request, 'band/landing.html')


def home(request):
    """
    This function renders the home page
    """
    return render(request, 'band/home.html')


def about(request):
    """
    This function renders the about page
    """
    return render(request, 'band/about.html')


def songs(request):
    """
    This function renders the songs page
    """
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'band/songs.html', context)