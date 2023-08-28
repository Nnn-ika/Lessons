from django.shortcuts import render
from .models import Advertisement

# Create your views here.
def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisement' : advertisement}
    return render(request, 'index.html', context)

def topSellers(request):
    return render(request, 'top-sellers.html')

def advertisementPost(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement(request):
    return render(request, 'advertisement.html')