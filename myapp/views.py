from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = "Fast"
    feature1.details = "Our service is very quick"

    context = {
      'name': 'Patrick',
      'age': 23,
      'nationality': 'British'
      }
    return render(request, 'index.html', {'feature': feature1})

def counter(request):
    words = request.POST['words']
    amt_of_word = len(words.split())
    context = {
        'amt': amt_of_word,
        'words': words
    }
    return render(request, 'counter.html', context)
    