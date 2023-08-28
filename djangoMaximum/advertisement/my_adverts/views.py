from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement
from django.utils.html import format_html

# Create your views here.
def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisement' : advertisement}
    return render(request, 'index.html', context)

def topSellers(request):
    return render(request, 'top-sellers.html')

def advertisementPost(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if title.startswith('?'):
                form.add_error('title', "Заголовок не может начинаться с символа '?'.")
            else:
                advertisement = Advertisement(**form.cleaned_data)
                advertisement.user = request.user
                advertisement.save()
                url = reverse('main_page')
                return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement(request):
    return render(request, 'advertisement.html')