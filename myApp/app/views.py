from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    name = "patrick"
    context = {
        'name': name,
        'age': 23,
        'Nationality': 'Rwanda'
    }
    return render(request, 'index.html', context)
