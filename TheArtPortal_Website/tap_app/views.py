from django.shortcuts import render
from .models import Artwork

def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'tap_app/home.html', {'artworks': artworks})

def login_view(request):
    return render(request, 'tap_app/login.html')

def ib_portfolios(request):
    return render(request, 'tap_app/ib_portfolios.html')

def other_portfolios(request):
    return render(request, 'tap_app/other_portfolios.html')

def artwork_form(request, category):
    return render(request, 'tap_app/artwork_form.html', {'category': category})