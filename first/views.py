from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'first/base.html')

def page(request):
    return render(request, 'first/random.html')