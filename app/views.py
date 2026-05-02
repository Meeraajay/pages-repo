from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render,redirect
from .models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback


# Create your views here.
def index(request):
    return render(request, 'landing.html')

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already taken'
            })

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('/login/')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
        feedbacks = Feedback.objects.filter(user = request.user ).order_by('-id')
        return render(request, 'dashboard.html', {
            'username': request.user.username,
            'password': request.user.password,
            'feedbacks': feedbacks,
        })

        

def logout_view(request):
    logout(request)
    return redirect('/') 

def delete_view(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('/')


def password(request):
    if request.method == "POST":
        username = request.session.get('username')
        new_password = request.POST.get('new_password')

        user = request.user
        user.set_password(new_password) 
        user.save()

        return redirect('/dashboard/')
    
    return render(request, 'password.html')


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            Feedback.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
                rating=form.cleaned_data['rating']
            )
            return redirect('/dashboard/')
        
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})