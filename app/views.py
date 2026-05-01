from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render,redirect
from .models import UserData

# Create your views here.
def index(request):
    return render(request, 'landing.html')

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserData(username=username, password=password)
        user.save()

        request.session['username'] = username

        return redirect('/login/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserData.objects.filter(username=username).first()

        if user and password == user.password:   
            request.session['username'] = username
            return redirect('/dashboard/')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def dashboard(request):
    username = request.session.get('username')

    user = UserData.objects.get(username=username)

    context = {
        'username': user.username,
        'password': user.password,
    }

    return render(request, 'dashboard.html', context)


def logout(request):
    request.session.flush()  
    return redirect('/') 

def delete(request):
    username = request.session.get('username')
    UserData.objects.all().delete()

    return redirect('/')


def password(request):
    if request.method == "POST":
        username = request.session.get('username')
        new_password = request.POST.get('new_password')

        user = UserData.objects.get(username=username)

        user.password = new_password
        user.save()

        return redirect('/dashboard/')
    
    return render(request, 'password.html')


    