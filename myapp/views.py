from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name='Anurag'
    return render(request, 'index.html', {'name': name})


def counter(request):
    text = request.GET['words']
    no_of_words = len(text.split())
    return render(request,'counter.html',{'amount':no_of_words} )