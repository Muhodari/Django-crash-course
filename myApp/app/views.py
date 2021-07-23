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


def counter(request):
    # text = request.GET['text']
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_of_words})
