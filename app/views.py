from django.shortcuts import render,redirect
from .models import UserData

# Create your views here.
def index(request):
    return render(request, 'landing.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = UserData.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            request.session['username'] = username
            request.session['password'] = password
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def dashboard(request):
    username = request.session.get('username')
    password = request.session.get('password')

    context = {
        'username': username,
        'password': password,
    }

    return render(request, 'dashboard.html', context)


def logout(request):
    request.session.flush()  
    return redirect('/') 