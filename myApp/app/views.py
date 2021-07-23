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

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'our services are very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'our services are very Reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.details = 'our services are Easy to  use '

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'our services are very affordable'

    features=[feature1,feature2,feature3,feature4]

    return render(request, 'static.html',
                  {'features':features})


def counter(request):
    # text = request.GET['text']
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
