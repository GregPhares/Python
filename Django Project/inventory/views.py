from django.shortcuts import render
from .models import *
from events.models import *


#from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_Amino(request):
    items = Amino.objects.all()
    context = {
        'items': items,
        'header':'Amino Acids',
    }
    return render(request, 'index.html', context)

def display_Bcaa(request):
    items = Bcaa.objects.all()
    context = {
        'items': items,
        'header': 'BCAA'
    }
    return render(request, 'index.html', context)


def display_Beta(request):
    items = Beta.objects.all()
    context = {
        'items': items,
        'header': 'Beta-Alanine'
    }
    return render(request, 'index.html', context)

def display_Caffeine(request):
    items = Caffeine.objects.all()
    context = {
        'items': items,
        'header':'Caffeine',
    }
    return render(request, 'index.html', context)

def display_LC(request):
    items = LC.objects.all()
    context = {
        'items': items,
        'header': 'L-Carnitine'
    }
    return render(request, 'index.html', context)


def display_NewOne(request):
    items = NewOne.objects.all()
    context = {
        'items': items,
        'header': 'New Items'
    }
    return render(request, 'index.html', context)


def display_Post(request):
    items = Post.objects.all()
    context = {
        'items': items,
        'header':'Post-Workout',
    }
    return render(request, 'index.html', context)

def display_Pre(request):
    items = Pre.objects.all()
    context = {
        'items': items,
        'header': 'Pre-Workout '
    }
    return render(request, 'index.html', context)


def display_Protein(request):
    items = Protein.objects.all()
    context = {
        'items': items,
        'header': 'Protein\'s'
    }
    return render(request, 'index.html', context)


def display_Recovery(request):
    items = Recovery.objects.all()
    context = {
        'items': items,
        'header': 'Body Recovery'
    }
    return render(request, 'index.html', context)


def display_Test(request):
    items = Test.objects.all()
    context = {
        'items': items,
        'header': 'Testosterone'
    }
    return render(request, 'index.html', context)