from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement
from django.utils.html import format_html

# Create your views here.
def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisement' : advertisement}
    return render(request, 'adverts_app/index.html', context)

def topSellers(request):
    return render(request, 'adverts_app/top-sellers.html')

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
                return redirect(reverse('main_page'))
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'adverts_app/advertisement-post.html', context)

def advertisement(request):
    return render(request, 'adverts_app/advertisement.html')