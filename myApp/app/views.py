from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


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


def counter(request):
    # text = request.GET['text']
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
