from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    name = "patrick"
    context = {
        'name': name,
        'age': 23,
        'Nationality': 'Rwanda'
    }
    # return render(request, 'index.html', context)
    # getting data from database
    features = Feature.objects.all()

    return render(request, 'static.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                redirect('login')
        else:
            messages.info(request, 'Password Not the same')
            redirect('register')
    else:
        return render(request, 'register.html')


def counter(request):
    # text = request.GET['text']c
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
