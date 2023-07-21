from datetime import datetime
from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
import requests
from .models import  WeatherData
from django.contrib.auth.models import User
import uuid          #for creating unique tokens
from .emails import send_emails
# Create your views here.

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(username = username).exists():
            messages.error(request, 'Username is already taken, try another name')
            return redirect('/register/')
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Email is already in use.')
            return redirect('/register/')
        if (password != cpassword):
            messages.error(request, " password didn't matched, try again")
            return redirect('/register/')
        

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        token = str(uuid.uuid4())
        if User.objects.filter(email = email).first():
            send_emails(email, token)
            messages.success(request, 'A conformation mail is sent. Login through mail')
            return redirect('/')
    return render(request, 'register.html')


def page1(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            messages.success(request, 'login Successful')
            return redirect('/homepage/')
        else:
            messages.error(request, 'Plese check username/password. Try again')
            return redirect('/')
    return render(request, 'login.html')

def mainpage(request):
    city = request.GET.get('city')
    #api = '895098b5d8379f2490a2922a5ca07143'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=895098b5d8379f2490a2922a5ca07143'
    data = requests.get(url).json()
    weather_data = WeatherData(
        description=data['weather'][0]['description'],
        temperature=data['main']['temp'],
        humidity=data['main']['humidity'],
        feels_like=data['main']['feels_like'],
        location=data['name'],
        datetime=timezone.now()
    )
    weather_data.save()
    details = {
        'location' : data['name'],
        'temperature_in_k' : data['main']['temp'],
        'temperature_in_c' : int(data['main']['temp']-273),
        'humidity': data['main']['humidity'],
        'feels_like': data['main']['feels_like'],
        'description': data['weather'][0]['description']
    }

    context = {'data' : details }
    print(context)
    return render(request, 'mainpage.html',context)