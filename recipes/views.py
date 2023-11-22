from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'Liedson Sales'
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return render(request, 'recipes/sobre.html')

def globall(request):
    return render(request, 'global/home.html', status=404)

# Create your views here.
